# Generated by Django 2.2.3 on 2019-10-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasection', '0017_datasetlisting_hero_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, help_text='Optional. Will be auto-generated from name if left blank.', max_length=255, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
