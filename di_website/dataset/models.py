from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from datetime import datetime

from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DecimalBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
    DateBlock
)
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

from .blocks import (
    MetaDataDescriptionBlock,
    MetaDataSourcesBlock,
)


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
    meta_data = StreamField([
        ('description', MetaDataDescriptionBlock(max_num=1)),
        ('sources', MetaDataSourcesBlock(max_num=1)),
    ], null=True, blank=True)
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
        InlinePanel('team_member_links', label="Dataset Author", max_num=1),
        StreamFieldPanel('meta_data'),
        MultiFieldPanel([
            FieldPanel('related_datasets_title'),
            InlinePanel('related_dataset_links', label="Related Datasets", max_num=MAX_RELATED_LINKS)
        ], heading='Related Dataset'),
        InlinePanel('more_about_links', label="More About Pages", max_num=MAX_RELATED_LINKS)
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['related_datasets'] = get_related_pages(self.related_dataset_links.all(), DatasetPage.objects)
        context['more_about_links'] = get_related_pages(self.more_about_links.all(), DatasetPage.objects)
        context['team_member_links'] = get_related_pages(self.team_member_links.all())

        return context


class DatasetPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='related_dataset_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'dataset.DatasetPage'
        ])
    ]


class MoreAboutRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='more_about_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]


class TeamMemberRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='team_member_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'ourteam.TeamMemberPage'
        ])
    ]
