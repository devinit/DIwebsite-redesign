# Generated by Django 2.2.2 on 2019-07-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190709_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='social_platform',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('linkedin', 'Linked In'), ('facebook', 'Facebook'), ('youtube', 'YouTube'), ('flickr', 'Flickr')], max_length=100),
        ),
    ]
