from django.db import models
from datetime import datetime

from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock, PageChooserBlock, TextBlock, StructBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class DataSetMixin(models.Model):
    class Meta():
        abstract = True

    parent_page_types = ['datasection.DataSetListing']
    subpage_types = []

    dataset_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    dataset_title = models.TextField(unique=True, blank=True, null=True)
    release_date = models.DateField(default=datetime.now)
    xlsx_link = models.URLField(blank=True, null=True)
    csv_link = models.URLField(blank=True, null=True)
    authors = StreamField([
        ('internal_author', PageChooserBlock(
            required=False,
            target_model='ourteam.TeamMemberPage',
            icon='fa-user'
        )),
        ('external_author', StructBlock([
            ('name', CharBlock(required=False)),
            ('title', CharBlock(required=False)),
            ('photograph', ImageChooserBlock(required=False)),
            ('page', URLBlock(required=False))
        ], icon='fa-user'))
    ], blank=True)
    meta_data = StreamField(
        [
            ('description', TextBlock(required=True)),
            ('provenance', TextBlock(required=False)),
            ('variables', TextBlock(required=False)),
            ('geography', TextBlock(required=False)),
            ('geograpic_coding', TextBlock(required=False)),
            ('unit', TextBlock(required=False)),
            ('internal_notes', TextBlock(required=False)),
            ('lead_analyst', TextBlock(required=False)),
            ('licence', TextBlock(required=False)),
            ('citation', TextBlock(required=False))
        ],
        verbose_name='Content',
        help_text='A description is expected, but only one of each shall be shown'
    )
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')


class DataSetSourceMixin(models.Model):
    class Meta():
        abstract = True

    source = models.ForeignKey(
        'datasection.DataSource', null=True, blank =True, on_delete=models.SET_NULL,
        related_name='+', verbose_name='Data Source')

    panels = [SnippetChooserPanel('source')]
