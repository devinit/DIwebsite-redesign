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
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from di_website.common.base import hero_panels, get_paginator_range, get_related_pages
from di_website.common.mixins import OtherPageMixin, HeroMixin, TypesetBodyMixin
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS

from taggit.models import Tag, TaggedItemBase

from modelcluster.fields import ParentalKey


class DataSectionPage(TypesetBodyMixin, HeroMixin, Page):
    """ Main page for datasets """

    content_panels = Page.content_panels + [
        hero_panels()
    ]

    parent_page_types = ['home.HomePage']

    class Meta:
        verbose_name = "Data Section Page"
