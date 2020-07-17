# Generated by Django 2.2.13 on 2020-07-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0018_auto_20200717_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartpage',
            name='title_in_image',
        ),
        migrations.AddField(
            model_name='chartpage',
            name='image_title',
            field=models.TextField(blank=True, help_text='Optional: appears in the image download at the bottom of the chart', null=True),
        ),
    ]
