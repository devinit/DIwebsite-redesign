# Generated by Django 2.2.2 on 2019-06-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20190618_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarymenulinks',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
