# Generated by Django 2.2.16 on 2020-09-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0032_auto_20200924_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedchartpage',
            name='d3_version',
            field=models.CharField(choices=[('v4', 'Version 4'), ('v5', 'Version 5'), ('v6', 'Version 6')], default='v4', max_length=50),
        ),
    ]