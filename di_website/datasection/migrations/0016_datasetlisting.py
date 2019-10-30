# Generated by Django 2.2.3 on 2019-10-17 08:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('datasection', '0015_auto_20191017_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetListing',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock())])), ('button_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.core.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.core.blocks.URLBlock(help_text='URL of the image source', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html'))], blank=True, null=True, verbose_name='Page Body')),
                ('other_pages_heading', models.CharField(blank=True, default='More about', max_length=255, verbose_name='Heading')),
            ],
            options={
                'verbose_name': 'DataSet Listing',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
