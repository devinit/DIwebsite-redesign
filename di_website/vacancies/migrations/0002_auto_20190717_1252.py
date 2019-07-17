# Generated by Django 2.2.2 on 2019-07-17 12:52

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancypage',
            name='downloads_description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Optional: a brief description of what to do in this section', verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='vacancypage',
            name='downloads_title',
            field=models.CharField(blank=True, default='Apply for this position', help_text='Title for the downloads section on a vacancy page', max_length=255, verbose_name='Title'),
        ),
    ]
