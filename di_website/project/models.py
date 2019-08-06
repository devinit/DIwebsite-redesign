from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    InlinePanel,
    PageChooserPanel,
    MultiFieldPanel,
    FieldPanel
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable, Page

from di_website.common.base import StandardPage, OtherPage
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_RELATED_LINKS

class ProjectPage(StandardPage):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )
    other_pages_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Section Title'
    )

    content_panels = StandardPage.content_panels + [
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('project_related_links', label="Related links", max_num=3)
        ], heading='Other Pages')
    ]

class ProjectPageRelatedLink(OtherPage):
    page = ParentalKey(Page, related_name='project_related_links', on_delete=models.CASCADE)
    panels = [
        PageChooserPanel('other_page')
    ]
