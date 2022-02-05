# Generated by Django 3.2.12 on 2022-02-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0072_auto_20220205_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancypage',
            name='application_close',
        ),
        migrations.AddField(
            model_name='vacancypage',
            name='application_close',
            field=models.DateField(blank=True, null=True, verbose_name='vacancies.ClosingDate'),
        ),
    ]
