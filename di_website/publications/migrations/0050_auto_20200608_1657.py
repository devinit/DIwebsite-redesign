# Generated by Django 3.0.7 on 2020-06-08 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0049_auto_20200514_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicationpagerelatedlink',
            options={'ordering': ['sort_order']},
        ),
    ]
