from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.contenttypes.models import ContentType

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from di_website.common.base import OtherPage, StandardPage, get_paginator_range
from di_website.common.blocks import BaseStreamBlock

from taggit.models import Tag, TaggedItemBase


class EventPage(StandardPage):
    """ Content of each event """

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100, help_text='Physical location of event')

    body = StreamField(BaseStreamBlock(), verbose_name="Page Body", blank=True)
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='Other pages in this section'
    )

    content_panels = StandardPage.content_panels + [
        MultiFieldPanel([
            FieldPanel('start_time'),
            FieldPanel('end_time'),
            FieldPanel('location')
        ], heading='Event Details'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Other Pages')
        ], heading='Other Pages')
    ]

    parent_page_types = ['EventIndexPage']

    class Meta:
        verbose_name = "Event Page"


class EventIndexPage(StandardPage):
    """ List of all events that have been created from events page """
    body = StreamField(BaseStreamBlock(), verbose_name="Page Body", blank=True)

    content_panels = StandardPage.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        events = EventPage.objects.live()

        paginator = Paginator(events, 10)
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
