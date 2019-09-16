# Generated by Django 2.2.4 on 2019-09-16 09:30

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0008_auto_20190916_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetpage',
            name='publication_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Publication Type'),
        ),
        migrations.AlterField(
            model_name='datasetpage',
            name='main_dataset_fields',
            field=wagtail.core.fields.StreamField([('release_date', wagtail.core.blocks.DateBlock()), ('text_content', wagtail.core.blocks.RichTextBlock(required=False)), ('most_recent_dataset', wagtail.core.blocks.PageChooserBlock(page_type=['dataset.DatasetPage'], required=False))], blank=True, help_text='These fields will fill up the top section of your dataset page.', verbose_name='Main Content'),
        ),
    ]
