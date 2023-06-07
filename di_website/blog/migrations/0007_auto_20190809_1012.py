# Generated by Django 2.2.3 on 2019-08-09 10:12

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190806_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticlepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('section_paragraph_block', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed'])), ('center', wagtail.blocks.BooleanBlock(default=False, required=False))])), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock())])), ('section_block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('center', wagtail.blocks.BooleanBlock(default=False, required=False))])), ('banner_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', required=False, template='blocks/embed_block.html')), ('text', wagtail.blocks.StreamBlock([('text', wagtail.blocks.TextBlock(template='blocks/banner/text.html')), ('list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock()), ('content', wagtail.blocks.TextBlock(required=False))], template='blocks/banner/list_item.html'), template='blocks/banner/list.html'))])), ('meta', wagtail.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))]))], required=False)), ('media_orientation', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False))]))], blank=True, null=True, verbose_name='Page Body'),
        ),
    ]
