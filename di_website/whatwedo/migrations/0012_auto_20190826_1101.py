# Generated by Django 2.2.3 on 2019-08-26 11:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('whatwedo', '0011_auto_20190826_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatwedopage',
            name='sections',
            field=wagtail.fields.StreamField([('locations_map', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(icon='fa-heading', required=False)), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', required=False, template='blocks/paragraph_block.html')), ('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))])), ('light', wagtail.blocks.BooleanBlock(default=False, help_text='Applies a lighter background to the section', required=False))])), ('focus_area', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(default='Our focus areas', icon='fa-heading', required=False)), ('focus_areas', wagtail.blocks.ListBlock(wagtail.blocks.TextBlock(icon='fa-text'), required=False)), ('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))])), ('light', wagtail.blocks.BooleanBlock(default=False, help_text='Applies a lighter background to the section', required=False))])), ('expertise', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(default='Our expertise', icon='fa-heading', required=False)), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', required=False, template='blocks/paragraph_block.html')), ('expertise_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', required=False, template='blocks/paragraph_block.html'))]), required=False)), ('light', wagtail.blocks.BooleanBlock(default=False, help_text='Applies a lighter background to the section', required=False))])), ('banner', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', required=False, template='blocks/embed_block.html')), ('text', wagtail.blocks.StreamBlock([('text', wagtail.blocks.TextBlock(template='blocks/banner/text.html')), ('list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock()), ('content', wagtail.blocks.TextBlock(required=False))], template='blocks/banner/list_item.html'), template='blocks/banner/list.html'))])), ('meta', wagtail.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))])), ('document_box', wagtail.blocks.StructBlock([('box_heading', wagtail.blocks.CharBlock(icon='title', required=False)), ('documents', wagtail.blocks.StreamBlock([('document', wagtail.documents.blocks.DocumentChooserBlock())], required=False)), ('dark_mode', wagtail.blocks.BooleanBlock(default=False, help_text='Red on white if unchecked. White on dark grey if checked.', required=False))]))], required=False)), ('media_orientation', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False)), ('light', wagtail.blocks.BooleanBlock(default=False, help_text='Sets the background to a lighter colour', required=False))])), ('duo', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Section heading', icon='fa-heading', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('side_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', required=True, template='blocks/paragraph_block.html')), ('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))]))])), ('testimonial', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('cite', wagtail.blocks.TextBlock(help_text='The source of the testimonial')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True, null=True, verbose_name='Sections'),
        ),
    ]
