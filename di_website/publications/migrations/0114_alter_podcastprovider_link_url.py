# Generated by Django 3.2.15 on 2022-09-29 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0113_auto_20220928_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastprovider',
            name='link_url',
            field=models.URLField(max_length=255),
        ),
    ]
