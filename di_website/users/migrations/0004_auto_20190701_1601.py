# Generated by Django 2.2.2 on 2019-07-01 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190628_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'verbose_name': 'Job Title', 'verbose_name_plural': 'Job Titles'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
