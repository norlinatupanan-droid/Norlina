from django.db import models


class Project(models.Model):
    """A project shown inside the Developer's Workshop. Edit these in /admin/."""

    name = models.CharField(max_length=120)
    description = models.TextField()
    role = models.CharField(max_length=120, blank=True)
    tech = models.CharField(max_length=250, blank=True, help_text="Comma-separated, e.g. Django, Figma")
    image = models.CharField(
        max_length=250, blank=True,
        help_text="Path inside the static folder, e.g. game/img/fitplan.webp (or a full https:// URL)",
    )
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech.split(",") if t.strip()]


class ContactMessage(models.Model):
    """Messages sent from the treasure chest contact form."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}> ({self.created_at:%Y-%m-%d})"
