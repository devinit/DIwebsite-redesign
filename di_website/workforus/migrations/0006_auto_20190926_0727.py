# Generated by Django 2.2.3 on 2019-09-26 07:27

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('workforus', '0005_auto_20190925_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workforuspage',
            name='team_stories',
            field=wagtail.fields.StreamField([('team_story', wagtail.blocks.StructBlock([('team_story_page', wagtail.blocks.PageChooserBlock(page_type=['general.General'], verbose_name='Story Page')), ('logo', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True, verbose_name='Team Stories'),
        ),
    ]
