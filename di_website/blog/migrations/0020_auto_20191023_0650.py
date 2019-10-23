# Generated by Django 2.2.2 on 2019-10-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20191011_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticlepage',
            name='hero_image_credit_name',
            field=models.TextField(blank=True, help_text='Name of source of image used in hero if any', null=True, verbose_name='Image credit name'),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='hero_image_credit_name',
            field=models.TextField(blank=True, help_text='Name of source of image used in hero if any', null=True, verbose_name='Image credit name'),
        ),
    ]
