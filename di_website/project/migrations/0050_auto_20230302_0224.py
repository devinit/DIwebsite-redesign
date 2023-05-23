# Generated by Django 3.2.16 on 2023-03-02 02:24

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0049_auto_20230302_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPageTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_page_topics', to='project.projectpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_projectpagetopic_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='projectpage',
            name='topics',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='project.ProjectPageTopic', to='taggit.Tag', verbose_name='Topics'),
        ),
    ]