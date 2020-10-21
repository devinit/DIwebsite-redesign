# Generated by Django 3.1 on 2020-10-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0078_auto_20201021_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationpage',
            name='hide_date',
            field=models.BooleanField(default=True, help_text='Should the date appear on related links items ?', verbose_name='Hide Related Links Date'),
        ),
    ]
