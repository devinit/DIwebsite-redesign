# Generated by Django 3.2.7 on 2022-01-31 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0052_pivottablerowhighlight_row_highlight_colour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pivottablerowhighlight',
            old_name='table',
            new_name='page',
        ),
    ]