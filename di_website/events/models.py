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

from di_website.common.base import hero_panels, get_paginator_range
from di_website.common.mixins import OtherPageMixin, HeroMixin
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS

from taggit.models import Tag, TaggedItemBase

from modelcluster.fields import ParentalKey


class EventPage(HeroMixin, Page):
    """ Content of each event """

    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100, help_text='Physical location of event')

    body = StreamField(BaseStreamBlock(), verbose_name="Page Body", blank=True)
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Section Heading',
        default='Related content',
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            FieldPanel('start_date'),
            FieldPanel('end_date'),
            FieldPanel('start_time'),
            FieldPanel('end_time'),
            FieldPanel('location')
        ], heading='Event Details'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('event_related_links', label='Related Pages', max_num=MAX_RELATED_LINKS)
        ], heading='Other Pages')
    ]

    parent_page_types = ['EventIndexPage']

    def get_related_pages(self):
        related_links = self.event_related_links.all()
        related_links_count = len(related_links)

        if related_links_count < MAX_RELATED_LINKS:
            difference = MAX_RELATED_LINKS - related_links_count
            related_pages = [link.other_page for link in related_links]
            id_list = [page.id for page in related_pages]
            event_objects = EventPage.objects.live()
            related_links = list(related_pages) + list(event_objects.exclude(id__in=id_list)[:difference])
        else:
            related_links = list([link.other_page for link in related_links])

        return related_links

    def get_context(self, request):
        context = super().get_context(request)

        context['related_pages'] = self.get_related_pages()

        return context

    class Meta:
        verbose_name = "Event Page"


class EventIndexPage(HeroMixin, Page):
    """ List of all events that have been created from events page """
    body = StreamField(BaseStreamBlock(), verbose_name="Page Body", blank=True)

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        events = EventPage.objects.live()

        paginator = Paginator(events, MAX_PAGE_SIZE)
        try:
            context['events'] = paginator.page(page)
        except PageNotAnInteger:
            context['events'] = paginator.page(1)
        except EmptyPage:
            context['events'] = paginator.page(paginator.num_pages)

        context['paginator_range'] = get_paginator_range(paginator, context['events'])

        return context

    class Meta:
        verbose_name = "Event Index Page"

    subpage_types = ['EventPage']


class EventPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='event_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'events.EventPage',
            'blog.BlogArticlePage',
            'news.NewsStoryPage'
        ])
    ]
