# Generated by Django 2.2.3 on 2019-10-17 11:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('datasection', '0019_auto_20191017_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSourceTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasource_topics', to='datasection.DataSource')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasection_datasourcetopic_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datasource',
            name='topics',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='datasection.DataSourceTopic', to='taggit.Tag', verbose_name='Topics'),
        ),
    ]
