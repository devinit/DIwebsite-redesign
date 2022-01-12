# Generated by Django 3.2.7 on 2021-10-11 06:42

import di_website.common.templatetags.string_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0091_auto_20211008_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationappendixpage',
            name='uuid',
            field=models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6),
        ),
        migrations.AlterField(
            model_name='publicationchapterpage',
            name='uuid',
            field=models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6),
        ),
        migrations.AlterField(
            model_name='publicationforewordpage',
            name='uuid',
            field=models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='uuid',
            field=models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6),
        ),
        migrations.AlterField(
            model_name='publicationsummarypage',
            name='uuid',
            field=models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6),
        ),
        migrations.AlterField(
            model_name='shortpublicationpage',
            name='uuid',
            field=models.CharField(default=di_website.common.templatetags.string_utils.uid, max_length=6),
        ),
    ]