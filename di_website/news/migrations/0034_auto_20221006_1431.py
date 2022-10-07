# Generated by Django 3.2.15 on 2022-10-06 14:31

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0033_auto_20210615_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacenterpage',
            name='body',
            field=wagtail.core.fields.StreamField([('anchor', wagtail.core.blocks.StructBlock([('anchor_id', wagtail.core.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('source', wagtail.core.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.core.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.core.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.core.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.TextBlock(icon='fa-text')), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='newsstorypage',
            name='body',
            field=wagtail.core.fields.StreamField([('anchor', wagtail.core.blocks.StructBlock([('anchor_id', wagtail.core.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('source', wagtail.core.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.core.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.core.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.core.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.TextBlock(icon='fa-text')), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, verbose_name='Page Body'),
        ),
    ]
