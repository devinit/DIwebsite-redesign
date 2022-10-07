from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin, TypesetBodyMixin
from .blocks import PlaceStreamBlock
from di_website.common.constants import MAX_OTHER_PAGES

from modelcluster.fields import ParentalKey


class PlacesPage(TypesetBodyMixin, HeroMixin, Page):
    class Meta():
        verbose_name = 'Places Page'

    places = StreamField(
        PlaceStreamBlock,
        verbose_name="Places",
        null=True,
        blank=True,
        use_json_field=True
    )
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('body'),
        FieldPanel('places'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages', max_num=MAX_OTHER_PAGES)
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['home.StandardPage', 'general.General']
    parent_page_types = ['whatwedo.WhatWeDoPage']

    # TODO: set Where we Work as parent page
