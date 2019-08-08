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
from wagtail.core.models import Page

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin, OtherPageMixin
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_RELATED_LINKS


class ProjectPage(BaseStreamBodyMixin, HeroMixin, Page):
    other_pages_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Section Title'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('project_related_links',
                        label="Related links", max_num=MAX_RELATED_LINKS)
        ], heading='Other Pages')
    ]


class ProjectPageRelatedLink(OtherPageMixin):
    page = ParentalKey(
        Page, related_name='project_related_links', on_delete=models.CASCADE)
    panels = [
        PageChooserPanel('other_page')
    ]
