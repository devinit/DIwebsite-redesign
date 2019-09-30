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


class EventPage(TypesetBodyMixin, HeroMixin, Page):
    """ Content of each event """

    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100, help_text='Physical location of event')
    registration_link = models.URLField(blank=True, null=True)

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
        FieldPanel('registration_link'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('event_related_links', label='Related Pages', max_num=MAX_RELATED_LINKS)
        ], heading='Other Pages'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['general.General']
    parent_page_types = ['EventIndexPage']

    def get_context(self, request):
        context = super().get_context(request)

        context['related_pages'] = get_related_pages(
            self.event_related_links.all(), EventPage.objects)

        return context

    class Meta:
        verbose_name = "Event Page"


class EventIndexPage(TypesetBodyMixin, HeroMixin, Page):
    """ List of all events that have been created from events page """

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        InlinePanel('page_notifications', label='Notifications')
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

    subpage_types = ['EventPage','general.General']


class EventPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='event_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'events.EventPage',
            'blog.BlogArticlePage',
            'news.NewsStoryPage'
        ])
    ]
