# Generated by Django 2.2.2 on 2019-11-18 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('ourteam', '0008_teammemberpage_other_pages_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteampage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image'),
        ),
    ]
