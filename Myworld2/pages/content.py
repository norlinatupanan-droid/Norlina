"""Projects come from the database (editable in /admin/) with a fallback to portfolio_data.py."""
from .assets import versioned_static

from .models import Project
from .portfolio_data import PROJECTS


def _image_url(path):
    if path and not path.startswith(("http://", "https://", "/")):
        return versioned_static(path)
    return path


def get_projects():
    rows = [
        {
            "name": p.name, "description": p.description, "role": p.role, "tech": p.tech_list,
            "image": p.image, "live_url": p.live_url, "repo_url": p.repo_url,
        }
        for p in Project.objects.all()
    ] or [dict(p) for p in PROJECTS]
    for row in rows:
        row["image"] = _image_url(row.get("image", ""))
    return rows
