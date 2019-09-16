# Generated by Django 2.2.4 on 2019-09-16 08:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0006_auto_20190916_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetpage',
            name='main_dataset_fields',
            field=wagtail.core.fields.StreamField([('publication_type', wagtail.core.blocks.CharBlock(required=False)), ('release_date', wagtail.core.blocks.DateBlock()), ('text_content', wagtail.core.blocks.RichTextBlock(required=False)), ('most_recent_dataset', wagtail.core.blocks.PageChooserBlock(page_type=['dataset.DatasetPage']))], blank=True, help_text='These fields will fill up the top section of your dataset page.', verbose_name='Main Content'),
        ),
    ]
