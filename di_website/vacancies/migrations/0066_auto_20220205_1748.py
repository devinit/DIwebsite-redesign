# Generated by Django 3.2.12 on 2022-02-05 17:48

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0065_closingdate_salaryscale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancypage',
            name='salary_scale',
        ),
        migrations.AddField(
            model_name='vacancypage',
            name='salary_scale',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='vacancies.SalaryScale'),
        ),
    ]
