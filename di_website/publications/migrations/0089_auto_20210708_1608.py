# Generated by Django 2.2.16 on 2021-07-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0088_auto_20210708_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationpage',
            name='read_online_button_text',
            field=models.CharField(blank=True, default='Read Online', max_length=256, null=True, verbose_name='Read Online'),
        ),
        migrations.AlterField(
            model_name='publicationpage',
            name='request_hard_copy_text',
            field=models.CharField(blank=True, default='Request a hard copy', max_length=256, null=True, verbose_name='Read Hard Copy'),
        ),
    ]