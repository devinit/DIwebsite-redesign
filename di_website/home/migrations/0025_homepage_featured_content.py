# Generated by Django 2.2.3 on 2019-09-20 08:05

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20190919_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.fields.StreamField([('area', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock()), ('related_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_caption', wagtail.blocks.CharBlock(help_text='Overwrite title text from the related page', required=False))]))], blank=True, null=True),
        ),
    ]
