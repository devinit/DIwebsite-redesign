# Generated by Django 2.2.4 on 2019-09-16 10:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0010_auto_20190916_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetpage',
            name='meta_data',
            field=wagtail.core.fields.StreamField([('description', wagtail.core.blocks.StructBlock([('paragraph', wagtail.core.blocks.CharBlock(icon='title', required=False))]))], blank=True, null=True),
        ),
    ]
