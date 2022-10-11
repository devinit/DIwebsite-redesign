# Generated by Django 3.2.15 on 2022-09-23 08:07

from django.db import migrations


def update_related_option_handler_to_lowercase(apps, schema_editor):
    publication = apps.get_model('publications', 'PublicationPage')
    foreword = apps.get_model('publications', 'PublicationForewordPage')
    summary = apps.get_model('publications', 'PublicationSummaryPage')
    chapter = apps.get_model('publications', 'PublicationChapterPage')
    appendix = apps.get_model('publications', 'PublicationAppendixPage')
    legacy = apps.get_model('publications', 'LegacyPublicationPage')
    short = apps.get_model('publications', 'ShortPublicationPage')
    audio = apps.get_model('publications', 'AudioVisualMedia')

    for item in [publication, foreword, summary, chapter, appendix, legacy, short, audio]:
        for pub in item.objects.all():
            pub.related_option_handler = pub.related_option_handler.lower()
            pub.save()


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0108_auto_20220923_0803'),
    ]

    operations = [
        migrations.RunPython(update_related_option_handler_to_lowercase),
    ]