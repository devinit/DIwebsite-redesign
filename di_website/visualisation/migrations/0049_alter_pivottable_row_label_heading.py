# Generated by Django 3.2.7 on 2022-01-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0048_pivottable_row_label_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pivottable',
            name='row_label_heading',
            field=models.CharField(blank=True, default='Row labels', help_text='Optional: heading of the row label column', max_length=200, null=True),
        ),
    ]
