# Generated by Django 2.2.13 on 2020-07-01 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0039_auto_20200701_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasectionpage',
            name='sections',
        ),
    ]
