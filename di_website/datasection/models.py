import random

from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel,
    PageChooserPanel, StreamFieldPanel
)
from wagtail.core.blocks import StreamBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from di_website.common.base import get_related_pages, hero_panels
from di_website.common.constants import MAX_RELATED_LINKS
from di_website.common.mixins import HeroMixin, OtherPageMixin, SectionBodyMixin, TypesetBodyMixin

from .blocks import QuoteStreamBlock


class DataSectionPage(SectionBodyMixin, TypesetBodyMixin, HeroMixin, Page):
    """ Main page for datasets """

    quotes = StreamField(
        QuoteStreamBlock,
        verbose_name="Quotes",
        null=True,
        blank=True
    )

    dataset_info = models.TextField(
        null=False,
        blank=False,
        default="",
        help_text='A description of the datasets'
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
        StreamFieldPanel('quotes'),
        FieldPanel('dataset_info'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['general.General']

    class Meta:
        verbose_name = "Data Section Page"

    def countQuotes(self):
        quote_counter = 0
        for quote in self.quotes:
            quote_counter = quote_counter + 1
        return quote_counter

    def getRandomQuote(self):
        number_of_quotes = self.countQuotes()
        if number_of_quotes == 1:
            for quote in self.quotes:
                return quote
        elif number_of_quotes >= 2:
            random_number = random.randint(0, number_of_quotes - 1)
            for index, quote in enumerate(self.quotes):
                if random_number == index:
                    return quote
        return

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['random_quote'] = self.getRandomQuote()
        return context
