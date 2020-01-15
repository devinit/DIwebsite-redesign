# Generated by Django 2.2.6 on 2020-01-15 11:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0003_auto_20200115_1117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colour',
            new_name='SpotlightColour',
        ),
        migrations.RenameModel(
            old_name='Source',
            new_name='SpotlightSource',
        ),
        migrations.AlterField(
            model_name='spotlightpage',
            name='themes',
            field=wagtail.core.fields.StreamField([('theme', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.TextBlock(required=True)), ('indicators', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('ddw_id', wagtail.core.blocks.CharBlock(label='DDW ID', max_length=255, required=True)), ('name', wagtail.core.blocks.TextBlock(required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='A description of this indicator')), ('source', wagtail.snippets.blocks.SnippetChooserBlock('spotlight.SpotlightSource')), ('color', wagtail.snippets.blocks.SnippetChooserBlock('spotlight.SpotlightColour')), ('start_year', wagtail.core.blocks.IntegerBlock()), ('end_year', wagtail.core.blocks.IntegerBlock()), ('range', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('value_prefix', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('value_suffix', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('tooltip_template', wagtail.core.blocks.TextBlock(help_text='Text for the tooltip.Template strings can be used to substitute values e.g. {name}', required=True))])))]))]),
        ),
    ]
