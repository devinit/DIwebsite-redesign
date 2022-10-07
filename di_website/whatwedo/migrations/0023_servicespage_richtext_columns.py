# Generated by Django 2.2.3 on 2019-10-10 15:00

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whatwedo', '0022_auto_20191009_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='richtext_columns',
            field=wagtail.fields.StreamField([('column', wagtail.blocks.StructBlock([('heading', wagtail.blocks.TextBlock(icon='title', required=False)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'anchor'], icon='fa-paragraph'))], template='blocks/richtext_column_text.html'))], blank=True, null=True),
        ),
    ]
