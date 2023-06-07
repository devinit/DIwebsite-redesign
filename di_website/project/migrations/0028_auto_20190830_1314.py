# Generated by Django 2.2.3 on 2019-08-30 13:14

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_auto_20190830_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock())])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False))]))], blank=True, null=True, verbose_name='Page Body'),
        ),
    ]
