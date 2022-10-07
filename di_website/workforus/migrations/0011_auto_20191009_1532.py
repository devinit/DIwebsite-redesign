# Generated by Django 2.2.2 on 2019-10-09 15:32

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('workforus', '0010_auto_20190930_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workforuspage',
            name='benefits',
            field=wagtail.fields.StreamField([('benefit', wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock()), ('body', wagtail.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('logo', wagtail.images.blocks.ImageChooserBlock(required=False))], blank=True, null=True, verbose_name='Benefits'),
        ),
    ]
