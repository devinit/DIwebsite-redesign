# Generated by Django 3.2.7 on 2022-01-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0092_auto_20211011_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortpublicationpage',
            name='use_state',
            field=models.BooleanField(default=False, help_text='Optional: add the global reactive mobx managed state'),
        ),
    ]