# Generated by Django 3.0.7 on 2020-06-25 06:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('blog', '0036_auto_20200608_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticlepage',
            name='internal_author_page',
            field=models.ForeignKey(blank=True, help_text="The author's page if the author has an internal profile. Photograph, job title, and page link will be drawn from this.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Internal Author'),
        ),
        migrations.AlterField(
            model_name='blogarticlepage',
            name='other_authors',
            field=wagtail.core.fields.StreamField([('internal_author', wagtail.core.blocks.PageChooserBlock(icon='user', label='Internal Author', page_type=['ourteam.TeamMemberPage'], required=False)), ('external_author', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('photograph', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.core.blocks.URLBlock(required=False))], icon='user', label='External Author'))], blank=True, help_text='Additional authors. If order is important, please use this instead of internal author page.', verbose_name='Other Authors'),
        ),
    ]
