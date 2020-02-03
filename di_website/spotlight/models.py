from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .snippets import SpotlightSource, SpotlightColour


class SpotlightPage(Page):
    class Meta():
        verbose_name = 'Spotlight Page'

    parent_page_types = ['datasection.DataSectionPage']

    country_code = models.CharField(max_length=100, help_text='e.g. UG, KE', default='')
    meta = models.ForeignKey(
        'spotlight.Spotlight',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('country_code')
        ], heading='Settings'),
        SnippetChooserPanel('meta'),
    ]
