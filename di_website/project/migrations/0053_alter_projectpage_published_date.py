# Generated by Django 3.2.15 on 2023-03-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0052_alter_focusareaspagelink_related_page_section_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='published_date',
            field=models.DateTimeField(blank=True, help_text='This date will be used for display and ordering', null=True),
        ),
    ]
