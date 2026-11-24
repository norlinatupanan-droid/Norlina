import json
import time

from django.http import JsonResponse
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from . import portfolio_data as data
from .content import get_projects
from .models import ContactMessage


@method_decorator(ensure_csrf_cookie, name="dispatch")
class HomePageView(TemplateView):
    """One scrolling page: hero, about, work, toolkit, contact."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            player=data.PROFILE,          # used by base.html for the page title and SEO tags
            profile=data.PROFILE,
            hero=data.HERO,
            about=data.ABOUT,
            hobbies=data.HOBBIES,
            tools=data.TOOLS,
            toolkit=data.TOOLKIT,
            projects=get_projects(),
            contact=data.CONTACT,
            contact_url=reverse("contact"),
        )
        return context


class ContactView(View):
    """Receives the treasure-chest form (JSON) and stores it for the admin to read."""

    MAX_PER_HOUR = 5

    def post(self, request):
        try:
            payload = json.loads(request.body.decode("utf-8") or "{}")
        except (ValueError, UnicodeDecodeError):
            return JsonResponse({"ok": False, "error": "Invalid request."}, status=400)

        if payload.get("website"):                       # honeypot: bots fill this in
            return JsonResponse({"ok": True})

        now = time.time()
        recent = [t for t in request.session.get("contact_times", []) if now - t < 3600]
        if len(recent) >= self.MAX_PER_HOUR:
            return JsonResponse({"ok": False, "error": "Too many messages. Please try again later."}, status=429)

        name = strip_tags(str(payload.get("name", ""))).strip()[:100]
        email = str(payload.get("email", "")).strip()[:254]
        message = strip_tags(str(payload.get("message", ""))).strip()[:2000]
        if not name or not message:
            return JsonResponse({"ok": False, "error": "Please fill in your name and message."}, status=400)
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({"ok": False, "error": "Please enter a valid email address."}, status=400)

        ContactMessage.objects.create(name=name, email=email, message=message)
        request.session["contact_times"] = recent + [now]
        return JsonResponse({"ok": True})
