# Generated by Django 3.2.15 on 2022-09-28 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0111_alter_podcastprovider_podcast'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podcastprovider',
            options={'ordering': ['sort_order'], 'verbose_name': 'Podcast Provider', 'verbose_name_plural': 'Podcast Providers'},
        ),
        migrations.RemoveField(
            model_name='podcastprovider',
            name='podcast',
        ),
    ]