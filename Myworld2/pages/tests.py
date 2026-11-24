import json

from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, Project
from .portfolio_data import HERO, HOBBIES, PROFILE


class HomePageTests(TestCase):
    def test_home_renders(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_main_sections_present(self):
        response = self.client.get(reverse("home"))
        for anchor in ("id=\"about\"", "id=\"work\"", "id=\"toolkit\"", "id=\"contact\""):
            self.assertContains(response, anchor)
        self.assertContains(response, PROFILE["full_name"])
        self.assertContains(response, '<a href="#top">Home</a>')
        self.assertContains(response, HERO["headline"][0])

    def test_static_files_are_cache_busted(self):
        html = self.client.get(reverse("home")).content.decode()
        self.assertRegex(html, r'site/css/site\.css\?v=\d+')
        self.assertRegex(html, r'site/js/site\.js\?v=\d+')

    def test_hobbies_rendered(self):
        response = self.client.get(reverse("home"))
        for item in HOBBIES["items"]:
            self.assertContains(response, item["label"])

    def test_seeded_projects_use_new_image_folder(self):
        self.assertEqual(Project.objects.count(), 3)
        self.assertFalse(Project.objects.filter(image__startswith="game/").exists())
        self.assertContains(self.client.get(reverse("home")), "site/img/fitplan.webp")

    def test_projects_come_from_database(self):
        Project.objects.all().delete()
        Project.objects.create(name="Test Quest", description="A DB project", tech="Django, Figma")
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Test Quest")
        self.assertNotContains(response, "I created this design using the Figma")

    def test_projects_fall_back_to_data_file(self):
        Project.objects.all().delete()
        self.assertContains(self.client.get(reverse("home")), "PALCONNECT")


class ContactTests(TestCase):
    def post(self, data):
        return self.client.post(reverse("contact"), json.dumps(data), content_type="application/json")

    def test_valid_message_is_saved(self):
        r = self.post({"name": "Ana", "email": "ana@example.com", "message": "Hello!"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_invalid_email_rejected(self):
        r = self.post({"name": "Ana", "email": "nope", "message": "Hello!"})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_honeypot_is_ignored(self):
        r = self.post({"name": "Bot", "email": "b@example.com", "message": "spam", "website": "x"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_rate_limit(self):
        for _ in range(5):
            self.post({"name": "Ana", "email": "ana@example.com", "message": "Hi"})
        self.assertEqual(self.post({"name": "Ana", "email": "ana@example.com", "message": "Hi"}).status_code, 429)

    def test_get_not_allowed(self):
        self.assertEqual(self.client.get(reverse("contact")).status_code, 405)
