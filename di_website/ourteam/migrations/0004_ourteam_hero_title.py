# Generated by Django 2.2.2 on 2019-07-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0003_auto_20190709_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='hero_title',
            field=models.CharField(blank=True, help_text='Leave blank if you want it to match the page title', max_length=255),
        ),
    ]
