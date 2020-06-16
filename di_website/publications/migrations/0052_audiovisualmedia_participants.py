# Generated by Django 3.0.7 on 2020-06-10 14:37

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0051_auto_20200608_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiovisualmedia',
            name='participants',
            field=wagtail.core.fields.StreamField([('internal_participant', wagtail.core.blocks.PageChooserBlock(icon='fa-user', label='Internal Participant', page_type=['ourteam.TeamMemberPage'], required=False)), ('external_participant', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('photograph', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.core.blocks.URLBlock(required=False))], icon='fa-user', label='External Participant'))], blank=True, help_text='The people involved in the podcast or webinar'),
        ),
    ]