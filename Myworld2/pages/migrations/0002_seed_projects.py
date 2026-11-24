from django.db import migrations

PROJECTS = [
    ("FITPLAN", "This is my recent work for my database class project about HRM or Human Resources Management.",
     "Database class project", "Database design, HRM", "game/img/fitplan.webp", 0),
    ("PALCONNECT", "I created this design using the Figma application and it's one of my favorite web designs for a landing page.",
     "UI designer", "Figma, Landing page", "game/img/palconnect.webp", 1),
    ("PSU FOOD RESERVATION APP", "An application to reserve food only at Palawan State University. I designed this for my Proposal project.",
     "UI designer", "Figma, App design", "game/img/psu-food.webp", 2),
]


def seed(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    if Project.objects.exists():
        return
    for name, description, role, tech, image, order in PROJECTS:
        Project.objects.create(name=name, description=description, role=role, tech=tech, image=image, order=order)


def unseed(apps, schema_editor):
    apps.get_model("pages", "Project").objects.filter(name__in=[p[0] for p in PROJECTS]).delete()


class Migration(migrations.Migration):
    dependencies = [("pages", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
