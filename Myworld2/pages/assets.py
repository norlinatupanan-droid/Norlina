"""Cache-busting for static files: adds ?v=<file modified time> so browsers never keep serving an old copy."""
from django.contrib.staticfiles import finders
from django.templatetags.static import static


def versioned_static(path):
    url = static(path)
    try:
        found = finders.find(path)
        if found:
            import os
            return f"{url}?v={int(os.path.getmtime(found))}"
    except Exception:
        pass
    return url
