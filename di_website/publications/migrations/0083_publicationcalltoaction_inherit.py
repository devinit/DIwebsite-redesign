# Generated by Django 2.2.16 on 2021-06-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0082_auto_20210618_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationcalltoaction',
            name='inherit',
            field=models.BooleanField(blank=True, default=False, help_text='Optional: show this CTA on child pages', null=True),
        ),
    ]