# Generated by Django 3.2.7 on 2022-01-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0043_auto_20220121_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pivottable',
            name='cell_highlight_condition',
            field=models.CharField(blank=True, choices=[('lt', 'Less Than'), ('gt', 'Greater Than')], default='lt', help_text='Optional: condition for highlighting cells', max_length=5, null=True, verbose_name='Cell Condition'),
        ),
        migrations.AlterField(
            model_name='pivottable',
            name='cell_highlight_value',
            field=models.IntegerField(blank=True, help_text='Optional: value to conditionally highlight cells', null=True, verbose_name='Cell value'),
        ),
        migrations.AlterField(
            model_name='pivottable',
            name='row_highlight_condition',
            field=models.CharField(blank=True, choices=[('lt', 'Less Than'), ('gt', 'Greater Than')], default='lt', help_text='Optional: condition for highlighting a row', max_length=5, null=True, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='pivottable',
            name='row_highlight_field',
            field=models.CharField(blank=True, help_text='Optional: column the value of which to conditionally highlight row', max_length=100, null=True, verbose_name='Column/Field'),
        ),
        migrations.AlterField(
            model_name='pivottable',
            name='row_highlight_value',
            field=models.IntegerField(blank=True, help_text='Optional: column value to conditionally highlight row', null=True, verbose_name='Column value'),
        ),
    ]
