# Generated by Django 2.2.3 on 2019-07-17 22:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero_title', models.CharField(blank=True, help_text='Leave blank if you want it to match the page title', max_length=255)),
                ('hero_image_credit_name', models.CharField(blank=True, help_text='Name of source of image used in hero if any', max_length=50, null=True, verbose_name='Image credit name')),
                ('hero_image_credit_url', models.URLField(blank=True, help_text='A Link to the original source of the image if any', null=True, verbose_name='Image credit url')),
                ('hero_text', wagtail.core.fields.RichTextField(blank=True, help_text='A description of the page content', null=True)),
                ('hero_link_caption', models.CharField(blank=True, help_text='Text to display on the link button', max_length=255)),
                ('hero_image', models.ForeignKey(blank=True, help_text='Hero Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_link', models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero link')),
            ],
            options={
                'verbose_name': 'What we do',
            },
            bases=('wagtailcore.page',),
        ),
    ]
