# Generated by Django 2.2.16 on 2021-06-17 13:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0079_auto_20210617_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationCallToAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('data_format', models.TextField(choices=[('top', 'Top'), ('bottom', 'Bottom')], default='plain', help_text='Options are plain, currency, percent', max_length=100)),
                ('title', models.CharField(blank=True, help_text='Optional: when left blank, the call to action will not be show', max_length=255, null=True, verbose_name='Title')),
                ('body', models.TextField(blank=True, help_text='Optional: describe the purpose of your call to action in a bit more detail', null=True, verbose_name='Description')),
                ('button_text', models.CharField(blank=True, help_text='Optional: this is required to show the button', max_length=255, null=True, verbose_name='Button Caption')),
                ('button_url', models.URLField(blank=True, help_text='Optional: this is required to show the button', max_length=255, null=True, verbose_name='Button URL')),
                ('position', models.CharField(blank=True, choices=[('top', 'Top'), ('bottom', 'Bottom')], default='top', max_length=100, null=True, verbose_name='Position')),
                ('item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication_cta', to='publications.PublicationPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]