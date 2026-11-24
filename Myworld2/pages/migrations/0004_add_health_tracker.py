from django.db import migrations


def add_health_tracker(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    if not Project.objects.filter(name="HEALTH TRACKER").exists():
        Project.objects.create(
            name="HEALTH TRACKER",
            description="A health tracking application designed to help users monitor their wellness and daily health activities.",
            role="UI designer",
            tech="Figma, App design",
            image="site/img/Health Tracker.png",
            order=0,
        )


def remove_health_tracker(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    Project.objects.filter(name="HEALTH TRACKER").delete()


class Migration(migrations.Migration):
    dependencies = [("pages", "0003_move_project_images")]

    operations = [
        migrations.RunPython(add_health_tracker, remove_health_tracker),
    ]
