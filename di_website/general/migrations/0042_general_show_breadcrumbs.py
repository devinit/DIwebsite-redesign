# Generated by Django 2.2.16 on 2020-09-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0041_auto_20200702_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False),
        ),
    ]
