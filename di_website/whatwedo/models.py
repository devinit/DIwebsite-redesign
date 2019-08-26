from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel)

from di_website.common.mixins import HeroMixin, TypesetBodyMixin
from di_website.common.base import hero_panels

from .blocks import ExpertiseBlock, FocusAreasBlock, LocationsMapBlock
from di_website.common.blocks import BannerBlock, TestimonialBlock, VideoDuoTextBlock
from di_website.common.constants import MAX_OTHER_PAGES

# Create your models here.
class WhatWeDoPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/07-what-we-do
    """

    class Meta:
        verbose_name = 'What We Do Page'

    sections = StreamField([
        ('locations_map', LocationsMapBlock()),
        ('focus_area', FocusAreasBlock()),
        ('expertise', ExpertiseBlock()),
        ('banner', BannerBlock()),
        ('duo', VideoDuoTextBlock()),
        ('testimonial', TestimonialBlock())
    ], verbose_name="Sections", null=True, blank=True)
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages', max_num=MAX_OTHER_PAGES)
        ], heading='Other Pages/Related Links')
    ]
