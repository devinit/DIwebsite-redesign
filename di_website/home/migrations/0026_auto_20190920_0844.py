# Generated by Django 2.2.3 on 2019-09-20 08:44

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_homepage_featured_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('related_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_caption', wagtail.core.blocks.CharBlock(help_text='Overwrite title text from the related page', required=False))], template='home/blocks/featured_content.html'))], blank=True, null=True),
        ),
    ]
