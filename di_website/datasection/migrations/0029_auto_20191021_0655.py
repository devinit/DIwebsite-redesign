# Generated by Django 2.2.3 on 2019-10-21 06:55

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0028_auto_20191018_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_datasets', to='datasection.DatasetPage'),
        ),
    ]
