# Generated by Django 2.2.4 on 2020-04-15 03:01

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('spotlight', '0033_countryspotlight_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryspotlight',
            name='country_spotlight',
            field=wagtail.fields.StreamField([('country_information', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.CharBlock(required=False))])), ('spotlight_page', wagtail.blocks.PageChooserBlock(page_type=['spotlight.SpotlightPage'], required=False))], blank=True, help_text='Add Country Spotlight.'),
        ),
        migrations.AddField(
            model_name='countryspotlight',
            name='spotlight_page',
            field=models.ForeignKey(blank=True, help_text='Country Spotlight Page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='countryspotlight',
            name='body',
            field=wagtail.fields.StreamField([('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('source', wagtail.blocks.TextBlock(help_text='Who is this quote acredited to?', required=False))])), ('button_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('link_block', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock(help_text='Leave blank if you wish to use the page title as a caption', required=False)), ('page', wagtail.blocks.PageChooserBlock(help_text='For the link/button to show, either this or the url are required', required=False)), ('url', wagtail.blocks.URLBlock(help_text='An alternative to an internal page', required=False))])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('credit_name', wagtail.blocks.CharBlock(help_text='Name of the image source', required=False)), ('credit_url', wagtail.blocks.URLBlock(help_text='URL of the image source', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Caption to appear beneath the image', required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-video-camera', required=False, template='blocks/embed_block.html'))], blank=True, null=True, verbose_name='Page Body'),
        ),
    ]
