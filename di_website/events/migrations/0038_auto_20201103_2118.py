# Generated by Django 3.1 on 2020-11-03 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_auto_20201103_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='time_and_location',
        ),
    ]
