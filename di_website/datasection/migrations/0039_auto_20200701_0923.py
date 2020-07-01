# Generated by Django 2.2.13 on 2020-07-01 09:23

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0038_auto_20200629_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasectionpage',
            name='dataset_info',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='A description of the datasets', null=True),
        ),
    ]
