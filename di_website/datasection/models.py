from django.db import models

import random

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import StreamBlock

from di_website.common.base import hero_panels, get_related_pages
from di_website.common.mixins import OtherPageMixin, HeroMixin, TypesetBodyMixin
from di_website.common.constants import MAX_RELATED_LINKS

from modelcluster.fields import ParentalKey

from .blocks import QuoteStreamBlock, DataSuportStreamBlock


class DataSectionPage(TypesetBodyMixin, HeroMixin, Page):
    """ Main page for datasets """

    quotes = StreamField(
        QuoteStreamBlock,
        verbose_name="Quotes",
        null=True,
        blank=True
    )

    dataset_subtitle = models.TextField(
        null=False,
        blank=False,
        default="",
        help_text='A description of the datasets'
    )

    data_support = StreamField(
        DataSuportStreamBlock(max_num=1),
        verbose_name="Data Support Services",
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('quotes'),
        FieldPanel('dataset_subtitle'),
        StreamFieldPanel('data_support'),
        InlinePanel('datasection_related_links',
            label='More About Us',
            max_num=MAX_RELATED_LINKS
        )

    ]

    parent_page_types = ['home.HomePage']

    class Meta:
        verbose_name = "Data Section Page"

    def getRandomQuote(self):
        random_number = random.randint(0, 2)
        counter = 0
        for quote in self.quotes:
            if random_number == counter:
                return quote
            counter = counter + 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['random_quote'] = self.getRandomQuote()
        context['related_pages'] = get_related_pages(self.datasection_related_links.all())
        return context


class DatasectionRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='datasection_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]
