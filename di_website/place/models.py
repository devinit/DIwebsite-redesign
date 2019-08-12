from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel
)

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin
from .blocks import PlaceStreamBlock

from modelcluster.fields import ParentalKey


class PlacesPage(BaseStreamBodyMixin, HeroMixin, Page):
    class Meta():
        verbose_name = 'Places Page'

    places = StreamField(
        PlaceStreamBlock,
        verbose_name="Places",
        null=True,
        blank=True
    )
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('places'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')
    ]

    subpage_types = ['home.StandardPage']

    # TODO: set Where we Work as parent page
