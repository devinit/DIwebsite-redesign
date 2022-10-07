# Generated by Django 2.2.4 on 2019-11-05 15:32

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whatwedo', '0035_auto_20191105_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhereWeWorkLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text='e.g. Bristol, UK | Kampala, UG | Nairobi, KE', max_length=100)),
                ('address', wagtail.fields.RichTextField(blank=True, help_text="E.g. 'North Quay House Quay Side, Temple Back Bristol, BS1 6FL, UK'", null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Locations Where We Work',
                'verbose_name_plural': 'Locations Where We Work',
                'db_table': 'locations_where_we_work',
            },
        ),
    ]
