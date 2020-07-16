# Generated by Django 2.2.3 on 2019-09-02 13:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('whatwedo', '0015_auto_20190902_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='sections',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'])), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('banner_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.TextBlock(template='blocks/banner/text.html')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.TextBlock(required=False))], template='blocks/banner/list_item.html'), template='blocks/banner/list.html'))])), ('meta', wagtail.core.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False))])), ('document_box', wagtail.core.blocks.StructBlock([('box_heading', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('documents', wagtail.core.blocks.StreamBlock([('document', wagtail.documents.blocks.DocumentChooserBlock())], required=False)), ('dark_mode', wagtail.core.blocks.BooleanBlock(default=False, help_text='Red on white if unchecked. White on dark grey if checked.', required=False))]))], required=False)), ('media_orientation', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False)), ('light', wagtail.core.blocks.BooleanBlock(default=False, help_text='Sets the background to a lighter colour', required=False))])), ('downloads', wagtail.core.blocks.StructBlock([('section_heading', wagtail.core.blocks.TextBlock(required=False)), ('section_sub_heading', wagtail.core.blocks.TextBlock(required=False)), ('document_box_heading', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('document_boxes', wagtail.core.blocks.StreamBlock([('document_box', wagtail.core.blocks.StructBlock([('box_heading', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('documents', wagtail.core.blocks.StreamBlock([('document', wagtail.documents.blocks.DocumentChooserBlock())], required=False)), ('dark_mode', wagtail.core.blocks.BooleanBlock(default=False, help_text='Red on white if unchecked. White on dark grey if checked.', required=False))]))], required=False))]))], blank=True, null=True, verbose_name='Sections'),
        ),
    ]
