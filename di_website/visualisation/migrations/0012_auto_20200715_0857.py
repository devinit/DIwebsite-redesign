# Generated by Django 2.2.13 on 2020-07-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0011_auto_20200707_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartpage',
            name='display_fallback_mobile',
            field=models.BooleanField(default=True, help_text='Optional: when selected devices with screen widths up to 400px will be served the fallback image', verbose_name='Show on mobile'),
        ),
        migrations.AlterField(
            model_name='chartpage',
            name='display_fallback_tablet',
            field=models.BooleanField(default=False, help_text='Optional: when selected devices with screen widths up to 700px will be served the fallback image', verbose_name='Show on tablet'),
        ),
        migrations.AlterField(
            model_name='chartpage',
            name='display_general_instructions',
            field=models.BooleanField(default=True, help_text='Optional: display the general visualisation instructions, edited on the visualisations parent page', verbose_name='Show instructions'),
        ),
    ]
