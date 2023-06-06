# Generated by Django 2.2.6 on 2020-04-26 08:44

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0060_auto_20200421_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotlightindicator',
            name='config',
            field=wagtail.fields.StreamField([('config', wagtail.blocks.StructBlock([('content', wagtail.blocks.TextBlock(classname='ace-editor-json-block', help_text='Enter your JSON here', label='JSON Content'))], max_num=1))], blank=True, null=True, verbose_name='JSON Config'),
        ),
    ]
