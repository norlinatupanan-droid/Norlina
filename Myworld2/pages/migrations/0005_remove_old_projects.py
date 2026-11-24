from django.db import migrations


def remove_old_projects(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(
        name__in=[
            "FITPLAN",
            "PALCONNECT",
            "PSU FOOD RESERVATION APP",
        ]
    ).delete()


def restore_old_projects(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    old_projects = [
        (
            "FITPLAN",
            "This is my recent work for my database class project about HRM or Human Resources Management.",
            "Database class project",
            "Database design, HRM",
            "site/img/fitplan.webp",
            1,
        ),
        (
            "PALCONNECT",
            "I created this design using the Figma application and it's one of my favorite web designs for a landing page.",
            "UI designer",
            "Figma, Landing page",
            "site/img/palconnect.webp",
            2,
        ),
        (
            "PSU FOOD RESERVATION APP",
            "An application to reserve food only at Palawan State University. I designed this for my Proposal project.",
            "UI designer",
            "Figma, App design",
            "site/img/psu-food.webp",
            3,
        ),
    ]
    for name, description, role, tech, image, order in old_projects:
        if not Project.objects.filter(name=name).exists():
            Project.objects.create(
                name=name,
                description=description,
                role=role,
                tech=tech,
                image=image,
                order=order,
            )


class Migration(migrations.Migration):
    dependencies = [("pages", "0004_add_health_tracker")]

    operations = [
        migrations.RunPython(remove_old_projects, restore_old_projects),
    ]
