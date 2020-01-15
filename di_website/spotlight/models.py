from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from .blocks import ThemeBlock
from .snippets import SpotlightSource, SpotlightColour


class SpotlightPage(Page):
    class Meta():
        verbose_name = 'Spotlight Page'

    parent_page_types = ['datasection.DataSectionPage']

    themes = StreamField([
        ('theme', ThemeBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('themes')
    ]
