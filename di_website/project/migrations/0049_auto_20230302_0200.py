# Generated by Django 3.2.16 on 2023-03-02 02:00

from django.db import migrations


def add_published_date(apps, schema_editor):
    project = apps.get_model('project', 'ProjectPage')
    for project_page in project.objects.all():
        if project_page.first_published_at is not None:
            project_page.published_date = project_page.first_published_at
            project_page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0048_auto_20230302_0159'),
    ]

    operations = [
        migrations.RunPython(add_published_date),
    ]
