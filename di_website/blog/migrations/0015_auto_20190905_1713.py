# Generated by Django 2.2.2 on 2019-09-05 17:13

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190905_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticlepage',
            name='other_authors',
            field=wagtail.fields.StreamField([('internal_author', wagtail.blocks.PageChooserBlock(page_type=['ourteam.TeamMemberPage'], required=False)), ('external_author', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=False)), ('photograph', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.blocks.URLBlock(required=False))]))], blank=True, help_text='Additional authors. If order is important, please use this instead of internal author page.'),
        ),
    ]
