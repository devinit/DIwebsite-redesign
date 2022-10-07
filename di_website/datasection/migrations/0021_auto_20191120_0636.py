# Generated by Django 2.2.6 on 2019-11-20 06:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0020_auto_20191118_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetpage',
            name='meta_data',
            field=wagtail.fields.StreamField([('description', wagtail.blocks.RichTextBlock(required=True)), ('provenance', wagtail.blocks.RichTextBlock(required=False)), ('variables', wagtail.blocks.RichTextBlock(required=False)), ('geography', wagtail.blocks.RichTextBlock(required=False)), ('geograpic_coding', wagtail.blocks.RichTextBlock(required=False)), ('unit', wagtail.blocks.RichTextBlock(required=False)), ('internal_notes', wagtail.blocks.RichTextBlock(required=False)), ('licence', wagtail.blocks.RichTextBlock(required=False)), ('citation', wagtail.blocks.RichTextBlock(required=False, template='blocks/urlize_richtext.html'))], help_text='A description is expected, but only one of each shall be shown', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='figurepage',
            name='meta_data',
            field=wagtail.fields.StreamField([('description', wagtail.blocks.RichTextBlock(required=True)), ('provenance', wagtail.blocks.RichTextBlock(required=False)), ('variables', wagtail.blocks.RichTextBlock(required=False)), ('geography', wagtail.blocks.RichTextBlock(required=False)), ('geograpic_coding', wagtail.blocks.RichTextBlock(required=False)), ('unit', wagtail.blocks.RichTextBlock(required=False)), ('internal_notes', wagtail.blocks.RichTextBlock(required=False)), ('licence', wagtail.blocks.RichTextBlock(required=False)), ('citation', wagtail.blocks.RichTextBlock(required=False, template='blocks/urlize_richtext.html'))], help_text='A description is expected, but only one of each shall be shown', verbose_name='Content'),
        ),
    ]
