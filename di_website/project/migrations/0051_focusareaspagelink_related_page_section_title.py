# Generated by Django 3.2.16 on 2023-03-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0050_auto_20230302_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='focusareaspagelink',
            name='related_page_section_title',
            field=models.CharField(blank=True, default='Key Projects and Publications', max_length=255, verbose_name='Section Title'),
        ),
    ]
