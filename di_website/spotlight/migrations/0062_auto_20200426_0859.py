# Generated by Django 2.2.6 on 2020-04-26 08:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0061_spotlightindicator_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotlightindicator',
            name='config',
            field=wagtail.core.fields.StreamField([('JSON', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.TextBlock(classname='ace-editor-json-block', help_text='Enter your JSON here', label='JSON Content'))]))], blank=True, null=True, verbose_name='JSON Config'),
        ),
    ]