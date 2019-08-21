from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel

from di_website.common.mixins import HeroMixin, TypesetBodyMixin
from di_website.common.base import hero_panels

# Create your models here.
class WhatWeDoPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/07-what-we-do
    """

    class Meta:
        verbose_name = 'What We Do Page'

    places_heading = models.CharField(
        blank=True, max_length=250, default='Where We Work', verbose_name='Heading')
    places_description = RichTextField(blank=True, verbose_name='Description')
    places_page = models.ForeignKey(
        'place.PlacesPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            FieldPanel('places_heading'),
            FieldPanel('places_description'),
            PageChooserPanel('places_page')
        ], heading='Where We Work Section')
    ]
