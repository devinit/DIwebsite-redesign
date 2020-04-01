from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.blocks import StreamBlock

from .snippets import SpotlightSource, SpotlightColour

from di_website.common.blocks import LinkBlock

class SpotlightPage(Page):
    class Meta():
        verbose_name = 'Spotlight Page'

    parent_page_types = ['datasection.DataSectionPage']

    country_code = models.CharField(max_length=100, help_text='e.g. UG, KE', default='')
    country_name = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=100, help_text='UGX, KES', default='')
    datasources_description = models.TextField(help_text='A description for data sources section', default='')
    datasources_links = StreamField([ ('link', LinkBlock()), ], null=True, blank=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('country_code'),
            FieldPanel('country_name'),
            FieldPanel('currency_code')
        ], heading='Settings'),
        MultiFieldPanel([
            FieldPanel('datasources_description'),
            StreamFieldPanel('datasources_links')
        ], heading='Data Sources Section')
    ]


class SpotlightTheme(Page):
    class Meta():
        verbose_name = 'Spotlight Theme'

    parent_page_types = [SpotlightPage]

    section = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text='Determines which section on the spotlights a particular theme and its indicators appears e.g map,facts')

    content_panels = Page.content_panels +  [
        FieldPanel('section'),
    ]

    search_fields = [
        index.SearchField('title')
    ]

    def get_admin_display_title(self):
        return '[' + self.section + '] - ' + self.title if self.section else self.title


class SpotlightIndicator(Page):
    class Meta():
        verbose_name = 'Spotlight Indicator'

    parent_page_types = [SpotlightTheme]

    ddw_id = models.CharField(max_length=255)
    description = models.TextField(help_text='A description of this indicator', null=True, blank=True)
    source = models.ForeignKey(
        SpotlightSource,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    color = models.ForeignKey(
        SpotlightColour,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    DATA_FORMAT_CHOICES = [
        ('percent', 'Percentage'),
        ('plain', 'Plain'),
        ('currency', 'Currency')
    ]
    data_format = models.TextField(
        max_length=100,
        choices=DATA_FORMAT_CHOICES,
        default='plain',
        help_text='Options are plain, currency, percent')
    range = models.CharField(max_length=100, null=True, blank=True, help_text='The range of values shown on the legend')
    value_prefix = models.CharField(max_length=100, null=True, blank=True)
    value_suffix = models.CharField(max_length=100, null=True, blank=True)
    tooltip_template = models.TextField(
        blank=True,
        null=True,
        help_text='Text for the tooltip.Template strings can be used to substitute values e.g. {name}')
    content_template = models.TextField(
        blank=True,
        null=True,
        default='',
        help_text='JSON config of the indicator content. A bit complex - talk to Edwin')

    content_panels = Page.content_panels +  [
        FieldPanel('ddw_id'),
        FieldPanel('description'),
        SnippetChooserPanel('source'),
        SnippetChooserPanel('color'),
        FieldPanel('start_year'),
        FieldPanel('end_year'),
        FieldPanel('data_format'),
        FieldPanel('range'),
        FieldPanel('value_prefix'),
        FieldPanel('value_suffix'),
        FieldPanel('tooltip_template'),
        FieldPanel('content_template')
    ]

    search_fields = [index.SearchField('ddw_id'), index.SearchField('title')]
