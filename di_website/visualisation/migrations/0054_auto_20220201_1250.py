# Generated by Django 3.2.7 on 2022-02-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0053_rename_table_pivottablerowhighlight_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pivottablerowhighlight',
            name='row_highlight_colour',
            field=models.CharField(blank=True, help_text='Optional: hex colour of highlighted row', max_length=256),
        ),
        migrations.AlterField(
            model_name='pivottablerowhighlight',
            name='row_highlight_field',
            field=models.CharField(blank=True, help_text='Optional: value of the column for which to conditionally highlight row', max_length=100, null=True, verbose_name='Column/Field'),
        ),
    ]