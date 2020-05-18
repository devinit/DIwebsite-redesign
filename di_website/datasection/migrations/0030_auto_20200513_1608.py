# Generated by Django 2.2.4 on 2020-05-13 16:08

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0029_auto_20200513_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasectionpage',
            name='sections',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'])), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('source', wagtail.core.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False)), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('banner_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_credit_name', wagtail.core.blocks.TextBlock(help_text='The name of the image source', required=False)), ('image_credit_url', wagtail.core.blocks.URLBlock(help_text='A link to the image source, if any', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('text', wagtail.core.blocks.StreamBlock([('text_heading', wagtail.core.blocks.CharBlock(icon='title', required=False, template='blocks/banner/text_heading.html')), ('text', wagtail.core.blocks.TextBlock(template='blocks/banner/text.html')), ('richtext', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], template='blocks/banner/richtext.html')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='An optional title to the list item', required=False)), ('content', wagtail.core.blocks.TextBlock(help_text='The list item content', required=True))], template='blocks/banner/list_item.html'), icon='list-ul', template='blocks/banner/list.html'))])), ('meta', wagtail.core.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('document_box', wagtail.core.blocks.StructBlock([('box_heading', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('documents', wagtail.core.blocks.StreamBlock([('document', wagtail.documents.blocks.DocumentChooserBlock())], required=False)), ('dark_mode', wagtail.core.blocks.BooleanBlock(default=False, help_text='Red on white if unchecked. White on dark grey if checked.', required=False))]))], required=False)), ('media_orientation', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False)), ('light', wagtail.core.blocks.BooleanBlock(default=False, help_text='Sets the background to a lighter colour', required=False))])), ('downloads', wagtail.core.blocks.StructBlock([('section_heading', wagtail.core.blocks.TextBlock(required=False)), ('section_sub_heading', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('document_box_heading', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('document_boxes', wagtail.core.blocks.StreamBlock([('document_box', wagtail.core.blocks.StructBlock([('box_heading', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('documents', wagtail.core.blocks.StreamBlock([('document', wagtail.documents.blocks.DocumentChooserBlock())], required=False)), ('dark_mode', wagtail.core.blocks.BooleanBlock(default=False, help_text='Red on white if unchecked. White on dark grey if checked.', required=False))]))], required=False)), ('alt', wagtail.core.blocks.BooleanBlock(default=True, help_text='White background if checked', required=False))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.core.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.core.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('image_duo', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.core.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.core.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False)), ('heading', wagtail.core.blocks.CharBlock(icon='fa-heading', required=False)), ('side_text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', required=True, template='blocks/paragraph_block.html')), ('button', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('alt', wagtail.core.blocks.BooleanBlock(default=False, help_text='White background if checked.', required=False))])), ('video_duo', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Section heading', icon='fa-heading', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('side_text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', required=True, template='blocks/paragraph_block.html')), ('button', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('alt', wagtail.core.blocks.BooleanBlock(default=False, help_text='White background if checked.', required=False))])), ('full_width_video_block', wagtail.core.blocks.StructBlock([('full_width', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/full_width_embed.html'))]))], blank=True, null=True, verbose_name='Sections'),
        ),
    ]