# Generated by Django 2.2.4 on 2019-09-16 11:53

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0017_auto_20190916_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetpage',
            name='meta_data',
            field=wagtail.core.fields.StreamField([('description', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(icon='title', required=False)), ('provenance', wagtail.core.blocks.RichTextBlock(icon='title', required=False)), ('variables', wagtail.core.blocks.RichTextBlock(icon='title', required=False)), ('geography', wagtail.core.blocks.RichTextBlock(icon='title', required=False)), ('topic', wagtail.core.blocks.RichTextBlock(icon='title', required=False))], max_num=1)), ('sources', wagtail.core.blocks.StructBlock([('data_sources', wagtail.core.blocks.PageChooserBlock(page_type=['dataset.DatasetPage'], required=False)), ('description', wagtail.core.blocks.RichTextBlock(icon='title', required=False))], max_num=1))], blank=True, null=True),
        ),
    ]
