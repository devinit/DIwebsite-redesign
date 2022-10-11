# Generated by Django 3.2.15 on 2022-10-07 10:12

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0046_auto_20221006_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasectionpage',
            name='body',
            field=wagtail.fields.StreamField([('anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='datasectionpage',
            name='quotes',
            field=wagtail.fields.StreamField([('team_member', wagtail.blocks.StructBlock([('quote_text', wagtail.blocks.TextBlock()), ('team_member', wagtail.blocks.PageChooserBlock(page_type=['ourteam.TeamMemberPage'], required=False))])), ('external_member', wagtail.blocks.StructBlock([('quote_text', wagtail.blocks.TextBlock()), ('name', wagtail.blocks.TextBlock()), ('role', wagtail.blocks.TextBlock()), ('organisation', wagtail.blocks.TextBlock()), ('external_member_photo', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Quotes'),
        ),
        migrations.AlterField(
            model_name='datasectionpage',
            name='tools',
            field=wagtail.fields.StreamField([('tool', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_credit_name', wagtail.blocks.TextBlock(help_text='The name of the image source', required=False)), ('image_credit_url', wagtail.blocks.URLBlock(help_text='A link to the image source, if any', required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('text', wagtail.blocks.StreamBlock([('text_heading', wagtail.blocks.CharBlock(icon='title', required=False, template='blocks/banner/text_heading.html')), ('text', wagtail.blocks.TextBlock(template='blocks/banner/text.html')), ('richtext', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], template='blocks/banner/richtext.html')), ('list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(help_text='An optional title to the list item', required=False)), ('content', wagtail.blocks.TextBlock(help_text='The list item content', required=True))], template='blocks/banner/list_item.html'), icon='list-ul', template='blocks/banner/list.html'))])), ('meta', wagtail.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('document_box', wagtail.blocks.StructBlock([('box_heading', wagtail.blocks.CharBlock(icon='title', required=False)), ('documents', wagtail.blocks.StreamBlock([('document', wagtail.documents.blocks.DocumentChooserBlock())], required=False)), ('dark_mode', wagtail.blocks.BooleanBlock(default=False, help_text='Red on white if unchecked. White on dark grey if checked.', required=False))]))], required=False)), ('media_orientation', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False)), ('light', wagtail.blocks.BooleanBlock(default=False, help_text='Sets the background to a lighter colour', required=False))], template='datasection/tools_banner_block.html'))], blank=True, null=True, use_json_field=True, verbose_name='Tools'),
        ),
        migrations.AlterField(
            model_name='datasetlisting',
            name='body',
            field=wagtail.fields.StreamField([('anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='datasetpage',
            name='authors',
            field=wagtail.fields.StreamField([('internal_author', wagtail.blocks.PageChooserBlock(icon='fa-user', page_type=['ourteam.TeamMemberPage'], required=False)), ('external_author', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=False)), ('photograph', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.blocks.URLBlock(required=False))], icon='fa-user'))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='datasetpage',
            name='body',
            field=wagtail.fields.StreamField([('anchor', wagtail.blocks.StructBlock([('anchor_id', wagtail.blocks.CharBlock(help_text='The unique indentifier for this anchor', required=True))])), ('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html')), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', required=True)), ('body', wagtail.blocks.TextBlock(help_text='Optional: describe the purpose of your call to action in a bit more detail', label='Description', required=False)), ('button_text', wagtail.blocks.CharBlock(help_text='Optional: this is required to show the button', label='Button Caption', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Optional: this is required to show the button', label='Button URL', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Optional: has priority over the button URL field', label='Button Page', required=False))])), ('accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.TextBlock(icon='fa-text')), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html'))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='datasetpage',
            name='meta_data',
            field=wagtail.fields.StreamField([('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=True)), ('provenance', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('variables', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('geography', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('geograpic_coding', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('unit', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('internal_notes', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('licence', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False)), ('citation', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], required=False, template='blocks/urlize_richtext.html'))], help_text='A description is expected, but only one of each shall be shown', use_json_field=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='authors',
            field=wagtail.fields.StreamField([('internal_author', wagtail.blocks.PageChooserBlock(icon='fa-user', page_type=['ourteam.TeamMemberPage'], required=False)), ('external_author', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=False)), ('photograph', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.blocks.URLBlock(required=False))], icon='fa-user'))], blank=True, use_json_field=True),
        ),
    ]