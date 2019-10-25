from django.db import models
from datetime import datetime

from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock, PageChooserBlock, RichTextBlock, StructBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock

class DataSetMixin(models.Model):
    class Meta():
        abstract = True

    parent_page_types = ['datasection.DataSetListing']
    subpage_types = []

    release_date = models.DateField(default=datetime.now)
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
            ('description', RichTextBlock(required=True)),
            ('provenance', RichTextBlock()),
            ('variables', RichTextBlock()),
            ('geography', RichTextBlock()),
            ('licence', RichTextBlock()),
            ('citation', RichTextBlock())
        ],
        verbose_name='Content',
        help_text='A description is expected, but only one of each shall be shown'
    )
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')
