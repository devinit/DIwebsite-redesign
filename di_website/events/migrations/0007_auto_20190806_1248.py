# Generated by Django 2.2.3 on 2019-08-06 12:48

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('events', '0006_auto_20190731_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventindexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed', 'blockquote'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('section_paragraph_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed', 'blockquote'])), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock())])), ('section_block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('banner_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', required=False, template='blocks/embed_block.html')), ('text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.TextBlock(template='blocks/banner/text.html')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.TextBlock(required=False))], template='blocks/banner/list_item.html'), template='blocks/banner/list.html'))])), ('meta', wagtail.core.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False))]))], required=False)), ('media_orientation', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False))]))], blank=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed', 'blockquote'], icon='fa-paragraph', template='blocks/paragraph_block.html')), ('section_paragraph_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'link', 'document', 'image', 'embed', 'blockquote'])), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock())])), ('section_block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('center', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('banner_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', required=False, template='blocks/embed_block.html')), ('text', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.TextBlock(template='blocks/banner/text.html')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.TextBlock(required=False))], template='blocks/banner/list_item.html'), template='blocks/banner/list.html'))])), ('meta', wagtail.core.blocks.CharBlock(help_text='Anything from a name, location e.t.c - usually to provide credit for the text', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False))]))], required=False)), ('media_orientation', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], required=False))]))], blank=True, verbose_name='Page Body'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='other_pages_heading',
            field=models.CharField(blank=True, default='Related content', max_length=255, verbose_name='Section Heading'),
        ),
        migrations.CreateModel(
            name='EventPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('other_page', models.ForeignKey(blank=True, help_text='A page to link to in the "Other Pages or Related Links" section', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_related_links', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
