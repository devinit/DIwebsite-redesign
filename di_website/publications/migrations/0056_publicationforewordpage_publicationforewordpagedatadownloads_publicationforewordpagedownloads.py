# Generated by Django 2.2.4 on 2020-06-17 07:49

import di_website.common.templatetags.string_utils
import di_website.publications.mixins
import di_website.social.models
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('downloads', '0001_initial'),
        ('wagtailimages', '0001_squashed_0021'),
        ('publications', '0055_merge_20200615_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationForewordPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero_image_credit_name', models.TextField(blank=True, help_text='Name of source of image used in hero if any', null=True, verbose_name='Image credit name')),
                ('hero_image_credit_url', models.URLField(blank=True, help_text='A Link to the original source of the image if any', null=True, verbose_name='Image credit url')),
                ('hero_text', wagtail.core.fields.RichTextField(blank=True, help_text='A description of the page content', null=True)),
                ('hero_link_caption', models.CharField(blank=True, help_text='Text to display on the link button', max_length=255)),
                ('uuid', models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6, unique=True)),
                ('highlight_image', models.BooleanField(blank=True, default=False)),
                ('content', wagtail.core.fields.StreamField([('captioned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 800px')), ('descriptive_text', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image', required=False)), ('caption', wagtail.core.blocks.TextBlock(help_text='Optional: caption text to appear below the image', required=False)), ('caption_link', wagtail.core.blocks.URLBlock(help_text='Optional: external link to appear below the image', required=False)), ('caption_label', wagtail.core.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))])), ('case_study', wagtail.core.blocks.StructBlock([('section_label', wagtail.core.blocks.CharBlock(default='Case Study')), ('heading', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.StreamBlock([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote'], label='WYSIWYG editor', required=False)), ('infographic', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Optional: heading for the infographic', required=False)), ('descriptive_text', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image or table', required=False)), ('images', wagtail.core.blocks.StreamBlock([('image_wide', wagtail.core.blocks.StructBlock([('wide', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 2400px'))], form_template='publications/block_forms/custom_struct.html', help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.', icon='image', label='Wide')), ('image_medium', wagtail.core.blocks.StructBlock([('medium', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1560px', required=False)), ('use_wide_image', wagtail.core.blocks.BooleanBlock(help_text='Optional: check this box to display the wide image at medium viewport sizes', required=False))], icon='image', label='Medium')), ('image_narrow', wagtail.core.blocks.StructBlock([('narrow', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1000px', required=False)), ('use_next_widest_image', wagtail.core.blocks.BooleanBlock(help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)', required=False))], icon='image', label='Narrow'))], block_counts={'image_medium': {'max_num': 1}, 'image_narrow': {'max_num': 1}, 'image_wide': {'max_num': 1, 'min_num': 1}}, max_num=3, min_num=1)), ('data', wagtail.core.blocks.StreamBlock([('long_description', wagtail.core.blocks.StructBlock([('long_description', wagtail.core.blocks.TextBlock(help_text='Infographics require a long description and/or tabular data'))], icon='bold', label='Long desc')), ('table', wagtail.core.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Infographics require a long description and/or tabular data'))], icon='list-ol', label='Table'))], block_counts={'long_description': {'max_num': 1}, 'table': {'max_num': 1}}, max_num=2, min_num=1)), ('caption', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the image or table', required=False)), ('caption_link', wagtail.core.blocks.URLBlock(help_text='Optional: external link to appear below the image or table', required=False)), ('caption_label', wagtail.core.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False)), ('downloads', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload', required=False), help_text='Optional: list of downloads to appear below the image or table'))], required=False)), ('captioned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 800px')), ('descriptive_text', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image', required=False)), ('caption', wagtail.core.blocks.TextBlock(help_text='Optional: caption text to appear below the image', required=False)), ('caption_link', wagtail.core.blocks.URLBlock(help_text='Optional: external link to appear below the image', required=False)), ('caption_label', wagtail.core.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))], required=False))]))])), ('definition_list', wagtail.core.blocks.StructBlock([('definitions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('term', wagtail.core.blocks.CharBlock()), ('definition', wagtail.core.blocks.TextBlock())]), icon='list-ul'))])), ('downloads', wagtail.core.blocks.StructBlock([('downloads', wagtail.core.blocks.StreamBlock([('file', wagtail.core.blocks.StructBlock([('file', wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload'))], icon='doc-empty', label='File')), ('url', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock())], icon='site', label='URL'))]))])), ('section_heading', wagtail.core.blocks.StructBlock([('section_id', wagtail.core.blocks.CharBlock(help_text='Prepended by a chapter number if available, this value should be unique to the page, e.g. "1", "1.1", "2", "2.1" etc.')), ('heading', wagtail.core.blocks.CharBlock())])), ('table', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('caption', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the table', required=False)), ('caption_link', wagtail.core.blocks.URLBlock(help_text='Optional: external link to appear below the table', required=False)), ('caption_label', wagtail.core.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False))])), ('rich_text', wagtail.core.blocks.StructBlock([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor', 'footnote']))])), ('infographic', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Optional: heading for the infographic', required=False)), ('descriptive_text', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: descriptive text to appear above the image or table', required=False)), ('images', wagtail.core.blocks.StreamBlock([('image_wide', wagtail.core.blocks.StructBlock([('wide', wagtail.images.blocks.ImageChooserBlock(help_text='Optimal minimum width 2400px'))], form_template='publications/block_forms/custom_struct.html', help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.', icon='image', label='Wide')), ('image_medium', wagtail.core.blocks.StructBlock([('medium', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1560px', required=False)), ('use_wide_image', wagtail.core.blocks.BooleanBlock(help_text='Optional: check this box to display the wide image at medium viewport sizes', required=False))], icon='image', label='Medium')), ('image_narrow', wagtail.core.blocks.StructBlock([('narrow', wagtail.images.blocks.ImageChooserBlock(help_text='Optional: optimal minimum width 1000px', required=False)), ('use_next_widest_image', wagtail.core.blocks.BooleanBlock(help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)', required=False))], icon='image', label='Narrow'))], block_counts={'image_medium': {'max_num': 1}, 'image_narrow': {'max_num': 1}, 'image_wide': {'max_num': 1, 'min_num': 1}}, max_num=3, min_num=1)), ('data', wagtail.core.blocks.StreamBlock([('long_description', wagtail.core.blocks.StructBlock([('long_description', wagtail.core.blocks.TextBlock(help_text='Infographics require a long description and/or tabular data'))], icon='bold', label='Long desc')), ('table', wagtail.core.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Infographics require a long description and/or tabular data'))], icon='list-ol', label='Table'))], block_counts={'long_description': {'max_num': 1}, 'table': {'max_num': 1}}, max_num=2, min_num=1)), ('caption', wagtail.core.blocks.RichTextBlock(features=['footnote'], help_text='Optional: caption text to appear below the image or table', required=False)), ('caption_link', wagtail.core.blocks.URLBlock(help_text='Optional: external link to appear below the image or table', required=False)), ('caption_label', wagtail.core.blocks.CharBlock(help_text='Optional: label for the caption link, defaults to the link if left blank', required=False)), ('downloads', wagtail.core.blocks.ListBlock(wagtail.snippets.blocks.SnippetChooserBlock('downloads.PublicationDownload', required=False), help_text='Optional: list of downloads to appear below the image or table'))]))])),
                ('excerpt_field', models.TextField(blank=True, verbose_name='Excerpt')),
                ('hero_image', models.ForeignKey(blank=True, help_text='Hero Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_link', models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero link')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Publications foreword',
            },
            bases=(di_website.social.models.MetadataPageMixin, wagtailmetadata.models.MetadataMixin, di_website.publications.mixins.PageSearchMixin, di_website.publications.mixins.UniqueForParentPageMixin, di_website.publications.mixins.FilteredDatasetMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PublicationForewordPageDownloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('download', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='downloads.PublicationDownload')),
                ('item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication_downloads', to='publications.PublicationForewordPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicationForewordPageDataDownloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('download', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='downloads.PublicationDownload')),
                ('item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_downloads', to='publications.PublicationForewordPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
