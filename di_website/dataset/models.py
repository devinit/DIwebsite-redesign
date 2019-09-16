from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from datetime import datetime

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from di_website.common.base import hero_panels, get_paginator_range, get_related_pages
from di_website.common.mixins import OtherPageMixin, HeroMixin, TypesetBodyMixin
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS

from taggit.models import Tag, TaggedItemBase

from modelcluster.fields import ParentalKey


class DatasetPage(TypesetBodyMixin, HeroMixin, Page):
    """ Content of each Dataset """

    publication_type = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Publication Type'
    )
    release_date = models.DateField(default=datetime.now)
    text_content = RichTextField(
        null=True,
        blank=True,
        verbose_name='Main Content',
        help_text='A description of the page content'
    )
    related_datasets_title = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Title'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('publication_type'),
        FieldPanel('release_date'),
        FieldPanel('text_content'),
        MultiFieldPanel([
            FieldPanel('related_datasets_title'),
            InlinePanel('related_dataset_links', label="Related Datasets", max_num=MAX_RELATED_LINKS)
        ], heading='Related Dataset')
    ]


class DatasetPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='related_dataset_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'dataset.DatasetPage'
        ])
    ]
