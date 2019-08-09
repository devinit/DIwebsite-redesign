from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin
from .blocks import PlaceStreamBlock


class PlacesPage(BaseStreamBodyMixin, HeroMixin, Page):
    class Meta():
        verbose_name = 'Places Page'

    places = StreamField(
        PlaceStreamBlock,
        verbose_name="Places",
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('places')
    ]

    # TODO: set Where we Work as parent page
