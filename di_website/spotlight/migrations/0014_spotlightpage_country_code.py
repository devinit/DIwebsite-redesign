# Generated by Django 2.2.6 on 2020-01-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0013_auto_20200117_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotlightpage',
            name='country_code',
            field=models.CharField(default='', help_text='e.g. UG, KE', max_length=100),
        ),
    ]
