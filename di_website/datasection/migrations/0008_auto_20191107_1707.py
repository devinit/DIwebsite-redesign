# Generated by Django 2.2.2 on 2019-11-07 17:07

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0007_auto_20191107_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetpage',
            name='meta_data',
            field=wagtail.fields.StreamField([('description', wagtail.blocks.TextBlock(required=True)), ('provenance', wagtail.blocks.TextBlock(required=False)), ('variables', wagtail.blocks.TextBlock(required=False)), ('geography', wagtail.blocks.TextBlock(required=False)), ('geograpic_coding', wagtail.blocks.TextBlock(required=False)), ('unit', wagtail.blocks.TextBlock(required=False)), ('internal_notes', wagtail.blocks.TextBlock(required=False)), ('lead_analyst', wagtail.blocks.TextBlock(required=False)), ('licence', wagtail.blocks.TextBlock(required=False)), ('citation', wagtail.blocks.TextBlock(required=False))], help_text='A description is expected, but only one of each shall be shown', verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='figurepage',
            name='meta_data',
            field=wagtail.fields.StreamField([('description', wagtail.blocks.TextBlock(required=True)), ('provenance', wagtail.blocks.TextBlock(required=False)), ('variables', wagtail.blocks.TextBlock(required=False)), ('geography', wagtail.blocks.TextBlock(required=False)), ('geograpic_coding', wagtail.blocks.TextBlock(required=False)), ('unit', wagtail.blocks.TextBlock(required=False)), ('internal_notes', wagtail.blocks.TextBlock(required=False)), ('lead_analyst', wagtail.blocks.TextBlock(required=False)), ('licence', wagtail.blocks.TextBlock(required=False)), ('citation', wagtail.blocks.TextBlock(required=False))], help_text='A description is expected, but only one of each shall be shown', verbose_name='Content'),
        ),
    ]
