# Generated by Django 2.2.4 on 2020-04-15 03:11

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0035_auto_20200415_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryspotlight',
            name='country_spotlight',
            field=wagtail.fields.StreamField([('country_information', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.CharBlock(required=False)), ('spotlight_page', wagtail.blocks.StreamBlock([('add_spotlight_page', wagtail.blocks.PageChooserBlock(page_type=['spotlight.SpotlightPage'], required=False))], blank=True, help_text='Add Page'))]))], blank=True, help_text='Add Country Spotlight.'),
        ),
    ]
