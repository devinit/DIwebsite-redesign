# Generated by Django 3.2.16 on 2022-10-12 12:14

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0041_auto_20221007_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventindexpage',
            name='body',
            field=wagtail.fields.StreamField([('anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='body',
            field=wagtail.fields.StreamField([('anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Page Body'),
        ),
    ]
