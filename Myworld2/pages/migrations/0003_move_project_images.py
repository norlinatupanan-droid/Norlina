from django.db import migrations


def forwards(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    for p in Project.objects.filter(image__startswith="game/img/"):
        p.image = p.image.replace("game/img/", "site/img/", 1)
        p.save(update_fields=["image"])


def backwards(apps, schema_editor):
    Project = apps.get_model("pages", "Project")
    for p in Project.objects.filter(image__startswith="site/img/"):
        p.image = p.image.replace("site/img/", "game/img/", 1)
        p.save(update_fields=["image"])


class Migration(migrations.Migration):
    dependencies = [("pages", "0002_seed_projects")]
    operations = [migrations.RunPython(forwards, backwards)]
