# Generated by Django 2.2.16 on 2020-10-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0036_auto_20200926_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedchartpage',
            name='use_echarts',
            field=models.BooleanField(blank=True, default=False, verbose_name='Use ECharts'),
        ),
    ]
