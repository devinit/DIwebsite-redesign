# Generated by Django 3.2.7 on 2022-01-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0040_auto_20210924_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedchartpage',
            name='subtitle',
            field=models.TextField(blank=True, help_text='Optional: subtitle to appear underneath the title.', null=True),
        ),
    ]