# Generated by Django 2.2.6 on 2020-04-26 13:17

from django.db import migrations

from di_website.common.blocks import AceEditorJSONBlock


def copy_to_config(apps, schema_editor):
    SpotlightIndicator = apps.get_model('spotlight', 'SpotlightIndicator')
    for indicator in SpotlightIndicator.objects.all():
        if indicator.content_template and not indicator.config:
            indicator.config = [('JSON', {'content':indicator.content_template})]
            indicator.save()


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0062_auto_20200426_0859'),
    ]

    operations = [
        migrations.RunPython(copy_to_config),
        migrations.RemoveField(
            model_name='spotlightindicator',
            name='content_template',
        ),
    ]
