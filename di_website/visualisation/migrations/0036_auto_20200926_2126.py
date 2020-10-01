# Generated by Django 2.2.16 on 2020-09-26 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('visualisation', '0035_auto_20200926_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancedchartpage',
            name='display_fallback_mobile',
            field=models.BooleanField(default=True, help_text='Optional: when selected devices with screen widths up to 400px will be served the fallback image', verbose_name='Show on mobile'),
        ),
        migrations.AddField(
            model_name='advancedchartpage',
            name='display_fallback_tablet',
            field=models.BooleanField(default=False, help_text='Optional: when selected devices with screen widths up to 700px will be served the fallback image', verbose_name='Show on tablet'),
        ),
        migrations.AddField(
            model_name='advancedchartpage',
            name='fallback_image',
            field=models.ForeignKey(help_text='Fallback image for the chart', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
