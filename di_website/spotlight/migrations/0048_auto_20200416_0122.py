# Generated by Django 2.2.4 on 2020-04-16 01:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0047_auto_20200416_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryspotlight',
            name='country_spotlight',
            field=wagtail.fields.StreamField([('country_information', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('spotlight_page', wagtail.blocks.StreamBlock([('add_spotlight_page', wagtail.blocks.PageChooserBlock(page_type=['spotlight.SpotlightPage'], required=False))], blank=True, help_text='Add Page', max_num=2, min_num=1)), ('background_theme', wagtail.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark')], help_text='Select background theme for this section'))]))], blank=True, help_text='Add Country Spotlight.'),
        ),
    ]
