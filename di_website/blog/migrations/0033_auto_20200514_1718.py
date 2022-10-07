# Generated by Django 2.2.4 on 2020-05-14 17:18

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200514_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticlepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], icon='fa-paragraph', template='blocks/paragraph_block_footnote.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('blog_infographic', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Optional: heading for the infographic', required=False)), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image or table', required=False)), ('images', wagtail.blocks.StreamBlock([('image_wide', wagtail.blocks.StructBlock([('wide', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 2400px'))], form_template='publications/block_forms/custom_struct.html', help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.', icon='image', label='Wide')), ('image_medium', wagtail.blocks.StructBlock([('medium', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1560px', required=False)), ('use_wide_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the wide image at medium viewport sizes', required=False))], icon='image', label='Medium')), ('image_narrow', wagtail.blocks.StructBlock([('narrow', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1000px', required=False)), ('use_next_widest_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)', required=False))], icon='image', label='Narrow'))], block_counts={'image_medium': {'max_num': 1}, 'image_narrow': {'max_num': 1}, 'image_wide': {'max_num': 1, 'min_num': 1}}, max_num=3, min_num=1)), ('data', wagtail.blocks.StreamBlock([('long_description', wagtail.blocks.StructBlock([('long_description', wagtail.blocks.TextBlock(help_text='Infographics require a long description and/or tabular data'))], icon='bold', label='Long desc')), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Infographics require a long description and/or tabular data'))], icon='list-ol', label='Table'))], block_counts={'long_description': {'max_num': 1}, 'table': {'max_num': 1}}, max_num=2, min_num=1)), ('caption', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the image or table', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image or table', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False)), ('downloads', wagtail.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload', required=False), help_text='Optional: list of downloads to appear below the image or table'))]))], blank=True, null=True, verbose_name='Page Body'),
        ),
    ]
