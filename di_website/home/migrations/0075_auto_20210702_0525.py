# Generated by Django 2.2.20 on 2021-07-02 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_cookienotice_link_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookienotice',
            old_name='link_title',
            new_name='title',
        ),
    ]
