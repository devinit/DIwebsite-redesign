# Generated by Django 3.2.7 on 2022-01-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0047_alter_pivottable_row_highlight_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='pivottable',
            name='row_label_heading',
            field=models.CharField(default='Row labels', help_text='Optional: heading of the row label column', max_length=200),
        ),
    ]