from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel)

from di_website.common.mixins import HeroMixin, TypesetBodyMixin
from di_website.common.base import hero_panels

from .blocks import FocusAreasBlock, LocationsMapBlock

# Create your models here.
class WhatWeDoPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/07-what-we-do
    """

    class Meta:
        verbose_name = 'What We Do Page'

    sections = StreamField([
        ('locations_map', LocationsMapBlock()),
        ('focus_area', FocusAreasBlock())
    ], verbose_name="Sections", null=True, blank=True)

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections')
    ]
