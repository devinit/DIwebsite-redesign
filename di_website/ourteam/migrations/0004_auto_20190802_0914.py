# Generated by Django 2.2.3 on 2019-08-02 09:14

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0003_remove_ourteampage_hero_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammemberpage',
            name='my_story',
            field=wagtail.fields.RichTextField(blank=True, help_text='Please say something about team member', null=True),
        ),
    ]
