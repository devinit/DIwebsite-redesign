# Generated by Django 3.2.7 on 2022-01-28 13:33

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0050_auto_20220125_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pivottable',
            name='row_highlight_condition',
        ),
        migrations.RemoveField(
            model_name='pivottable',
            name='row_highlight_field',
        ),
        migrations.RemoveField(
            model_name='pivottable',
            name='row_highlight_value',
        ),
        migrations.CreateModel(
            name='PivotTableRowHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('row_highlight_field', models.CharField(blank=True, help_text='Optional: column the value of which to conditionally highlight row', max_length=100, null=True, verbose_name='Column/Field')),
                ('row_highlight_condition', models.CharField(blank=True, choices=[('lt', 'Less Than'), ('gt', 'Greater Than'), ('eq', 'Equals'), ('lte', 'Less Than or Equal'), ('gte', 'Greater Than or Equal')], default='lt', help_text='Optional: condition for highlighting a row', max_length=5, null=True, verbose_name='Condition')),
                ('row_highlight_value', models.CharField(blank=True, help_text='Optional: column value to conditionally highlight row', max_length=200, null=True, verbose_name='Column value')),
                ('table', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='row_highlights', to='visualisation.pivottable')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
