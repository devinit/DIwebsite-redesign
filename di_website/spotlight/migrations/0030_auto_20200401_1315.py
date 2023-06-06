# Generated by Django 2.2.6 on 2020-04-01 13:15

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0029_auto_20200401_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotlightpage',
            name='datasources_description',
            field=models.TextField(blank=True, help_text='A description for data sources section', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='spotlightpage',
            name='datasources_links',
            field=wagtail.fields.StreamField([('link', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))]))], blank=True, null=True, verbose_name='Links'),
        ),
    ]
