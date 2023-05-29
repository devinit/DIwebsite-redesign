# Generated by Django 3.2.16 on 2023-05-29 09:18

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0124_auto_20230519_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationforewordpage',
            name='content',
            field=wagtail.fields.StreamField([('captioned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 800px')), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image', required=False)), ('caption', wagtail.blocks.TextBlock(help_text='Optional: caption text to appear below the image', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))])), ('case_study', wagtail.blocks.StructBlock([('section_label', wagtail.blocks.CharBlock(default='Case Study')), ('heading', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.StreamBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], label='WYSIWYG editor', required=False)), ('infographic', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Optional: heading for the infographic', required=False)), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image or table', required=False)), ('images', wagtail.blocks.StreamBlock([('image_wide', wagtail.blocks.StructBlock([('wide', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 2400px'))], form_template='publications/block_forms/custom_struct.html', help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.', icon='image', label='Wide')), ('image_medium', wagtail.blocks.StructBlock([('medium', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1560px', required=False)), ('use_wide_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the wide image at medium viewport sizes', required=False))], icon='image', label='Medium')), ('image_narrow', wagtail.blocks.StructBlock([('narrow', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1000px', required=False)), ('use_next_widest_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)', required=False))], icon='image', label='Narrow'))], block_counts={'image_medium': {'max_num': 1}, 'image_narrow': {'max_num': 1}, 'image_wide': {'max_num': 1, 'min_num': 1}}, max_num=3, min_num=1)), ('data', wagtail.blocks.StreamBlock([('long_description', wagtail.blocks.StructBlock([('long_description', wagtail.blocks.TextBlock(help_text='Infographics require a long description and/or tabular data'))], icon='bold', label='Long desc')), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Infographics require a long description and/or tabular data'))], icon='list-ol', label='Table'))], block_counts={'long_description': {'max_num': 1}, 'table': {'max_num': 1}}, max_num=2, min_num=1)), ('caption', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the image or table', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image or table', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False)), ('downloads', wagtail.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload', required=False), help_text='Optional: list of downloads to appear below the image or table')), ('full_width', wagtail.blocks.BooleanBlock(default=True, help_text='Optional: uncheck this box to match inforgraphic width to block content width', required=False)), ('interactive_chart_url', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='Link to be used to navigate to the interactive version of the chart', required=False)), ('button_caption', wagtail.blocks.CharBlock(default='Navigate to interactive chart', help_text='Caption to add to button that navigates to interactive chart', required=False))]))], required=False)), ('captioned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 800px')), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image', required=False)), ('caption', wagtail.blocks.TextBlock(help_text='Optional: caption text to appear below the image', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))], required=False))]))])), ('definition_list', wagtail.blocks.StructBlock([('definitions', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('term', wagtail.blocks.CharBlock()), ('definition', wagtail.blocks.TextBlock())]), icon='list-ul'))])), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False)), ('center', wagtail.blocks.BooleanBlock(default=False, required=False))], template='blocks/publication_blockquote.html')), ('downloads', wagtail.blocks.StructBlock([('downloads', wagtail.blocks.StreamBlock([('file', wagtail.blocks.StructBlock([('file', wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload'))], icon='doc-empty', label='File')), ('url', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock())], icon='site', label='URL'))]))])), ('section_heading', wagtail.blocks.StructBlock([('section_id', wagtail.blocks.CharBlock(help_text='Prepended by a chapter number if available, this value should be unique to the page, e.g. "1", "1.1", "2", "2.1" etc.')), ('heading', wagtail.blocks.CharBlock())])), ('table', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('caption', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the table', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the table', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))])), ('pivot_table', wagtail.blocks.StructBlock([('show_title', wagtail.blocks.BooleanBlock(default=True, required=False)), ('pivot_table', wagtail.blocks.PageChooserBlock(page_type=['visualisation.PivotTable']))])), ('dynamic_table', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('data_source_url', wagtail.blocks.URLBlock(help_text='Link to the CSV data file')), ('caption', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the table', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the table', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))])), ('rich_text', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote']))])), ('infographic', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Optional: heading for the infographic', required=False)), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image or table', required=False)), ('images', wagtail.blocks.StreamBlock([('image_wide', wagtail.blocks.StructBlock([('wide', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 2400px'))], form_template='publications/block_forms/custom_struct.html', help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.', icon='image', label='Wide')), ('image_medium', wagtail.blocks.StructBlock([('medium', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1560px', required=False)), ('use_wide_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the wide image at medium viewport sizes', required=False))], icon='image', label='Medium')), ('image_narrow', wagtail.blocks.StructBlock([('narrow', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1000px', required=False)), ('use_next_widest_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)', required=False))], icon='image', label='Narrow'))], block_counts={'image_medium': {'max_num': 1}, 'image_narrow': {'max_num': 1}, 'image_wide': {'max_num': 1, 'min_num': 1}}, max_num=3, min_num=1)), ('data', wagtail.blocks.StreamBlock([('long_description', wagtail.blocks.StructBlock([('long_description', wagtail.blocks.TextBlock(help_text='Infographics require a long description and/or tabular data'))], icon='bold', label='Long desc')), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Infographics require a long description and/or tabular data'))], icon='list-ol', label='Table'))], block_counts={'long_description': {'max_num': 1}, 'table': {'max_num': 1}}, max_num=2, min_num=1)), ('caption', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the image or table', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image or table', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False)), ('downloads', wagtail.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload', required=False), help_text='Optional: list of downloads to appear below the image or table')), ('full_width', wagtail.blocks.BooleanBlock(default=True, help_text='Optional: uncheck this box to match inforgraphic width to block content width', required=False)), ('interactive_chart_url', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='Link to be used to navigate to the interactive version of the chart', required=False)), ('button_caption', wagtail.blocks.CharBlock(default='Navigate to interactive chart', help_text='Caption to add to button that navigates to interactive chart', required=False))]))])), ('anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('interactive_chart', wagtail.blocks.StructBlock([('chart_page', wagtail.blocks.PageChooserBlock(page_type=['visualisation.ChartPage']))])), ('advanced_interactive_chart', wagtail.blocks.StructBlock([('show_title', wagtail.blocks.BooleanBlock(default=True, required=False)), ('allow_share', wagtail.blocks.BooleanBlock(default=True, required=False)), ('chart_page', wagtail.blocks.PageChooserBlock(page_type=['visualisation.AdvancedChartPage', 'visualisation.RawCodePage']))])), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))])), ('so_what', wagtail.blocks.StructBlock([('section_label', wagtail.blocks.CharBlock(default='So What')), ('heading', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.StreamBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], label='WYSIWYG editor', required=False)), ('infographic', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Optional: heading for the infographic', required=False)), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image or table', required=False)), ('images', wagtail.blocks.StreamBlock([('image_wide', wagtail.blocks.StructBlock([('wide', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 2400px'))], form_template='publications/block_forms/custom_struct.html', help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.', icon='image', label='Wide')), ('image_medium', wagtail.blocks.StructBlock([('medium', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1560px', required=False)), ('use_wide_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the wide image at medium viewport sizes', required=False))], icon='image', label='Medium')), ('image_narrow', wagtail.blocks.StructBlock([('narrow', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1000px', required=False)), ('use_next_widest_image', wagtail.blocks.BooleanBlock(help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)', required=False))], icon='image', label='Narrow'))], block_counts={'image_medium': {'max_num': 1}, 'image_narrow': {'max_num': 1}, 'image_wide': {'max_num': 1, 'min_num': 1}}, max_num=3, min_num=1)), ('data', wagtail.blocks.StreamBlock([('long_description', wagtail.blocks.StructBlock([('long_description', wagtail.blocks.TextBlock(help_text='Infographics require a long description and/or tabular data'))], icon='bold', label='Long desc')), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Infographics require a long description and/or tabular data'))], icon='list-ol', label='Table'))], block_counts={'long_description': {'max_num': 1}, 'table': {'max_num': 1}}, max_num=2, min_num=1)), ('caption', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the image or table', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image or table', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False)), ('downloads', wagtail.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload', required=False), help_text='Optional: list of downloads to appear below the image or table')), ('full_width', wagtail.blocks.BooleanBlock(default=True, help_text='Optional: uncheck this box to match inforgraphic width to block content width', required=False)), ('interactive_chart_url', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='Link to be used to navigate to the interactive version of the chart', required=False)), ('button_caption', wagtail.blocks.CharBlock(default='Navigate to interactive chart', help_text='Caption to add to button that navigates to interactive chart', required=False))]))], required=False)), ('captioned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 800px')), ('descriptive_text', wagtail.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image', required=False)), ('caption', wagtail.blocks.TextBlock(help_text='Optional: caption text to appear below the image', required=False)), ('caption_link', wagtail.blocks.URLBlock(help_text='Optional: external link to appear below the image', required=False)), ('caption_label', wagtail.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))], required=False))])), ('authors', wagtail.blocks.StreamBlock([('internal_author', wagtail.blocks.PageChooserBlock(icon='user', label='Internal Author', page_type=['ourteam.TeamMemberPage'], required=False)), ('external_author', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=False)), ('photograph', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.blocks.URLBlock(required=False))], icon='user', label='External Author'))], blank=True, use_json_field=True, verbose_name='Authors'))])), ('video', wagtail.blocks.StructBlock([('video_url', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g. https://www.youtube.com/embed/SGJFWirQ3ks', required=False))]))], use_json_field=True),
        ),
    ]
