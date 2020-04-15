from django.db import models

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    StructBlock,
    StreamBlock,
    RichTextBlock,
    ChoiceBlock
)

from .snippets import SpotlightSource, SpotlightColour

from di_website.common.blocks import LinkBlock
from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin, TypesetBodyMixin
from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES


class SpotlightPage(Page):
    class Meta():
        verbose_name = 'Spotlight Page'

    parent_page_types = ['spotlight.CountrySpotlight']

    country_code = models.CharField(max_length=100, help_text='e.g. UG, KE', default='')
    country_name = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=100, help_text='UGX, KES', default='')
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        help_text='Optional: a brief description about this page',
    )
    datasources_description = models.TextField(
        help_text='A description for data sources section', null=True, blank=True, verbose_name='Description')
    datasources_links = StreamField([ ('link', LinkBlock()), ], null=True, blank=True, verbose_name='Links')
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('country_code'),
            FieldPanel('country_name'),
            FieldPanel('currency_code'),
            FieldPanel('description')
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
    excluded_years = models.TextField(help_text='Comma separated values e.g. 2002,2004,2017', blank=True, null=True)
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
        FieldPanel('excluded_years'),
        FieldPanel('data_format'),
        FieldPanel('range'),
        FieldPanel('value_prefix'),
        FieldPanel('value_suffix'),
        FieldPanel('tooltip_template'),
        FieldPanel('content_template')
    ]

    search_fields = [index.SearchField('ddw_id'), index.SearchField('title')]


class CountrySpotlight(TypesetBodyMixin, HeroMixin, Page):
    spotlight_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Country Spotlight Page"
    )
    add_country_spotlight = StreamBlock([
        ('add_spotlight_page', PageChooserBlock(required=False, target_model='spotlight.SpotlightPage')),
    ], blank=True, help_text="Add Page")
    country_spotlight = StreamField([
        ('country_information', StructBlock([
            ('title', CharBlock(required=False)),
            ('description', RichTextBlock(
                icon='fa-paragraph',
                template='blocks/paragraph_block.html',
                features=RICHTEXT_FEATURES_NO_FOOTNOTES
            )),
            ('spotlight_page', add_country_spotlight),
            ('background_theme', ChoiceBlock(choices=[
                ('light', 'Light'),
                ('dark', 'Dark'),
            ], help_text='Select background theme for this section')),
        ])),
    ], blank=True, help_text="Add Country Spotlight.")

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('country_spotlight'),
    ]

    parent_page_types = ['datasection.DataSectionPage']
    subpage_types = ['spotlight.SpotlightPage']

    class Meta():
        verbose_name = 'Country Spotlight'
