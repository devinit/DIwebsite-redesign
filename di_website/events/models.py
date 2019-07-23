from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, StreamFieldPanel)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from di_website.common.base import OtherPage, StandardPage
from di_website.common.blocks import BaseStreamBlock

""" Content of each Event that makes up events list """


class EventPage(StandardPage):

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(
        max_length=100, help_text='Physical location of event')

    body = StreamField(BaseStreamBlock(), verbose_name="Page Body", blank=True)
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='Other pages in this section')

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

    parent_page_types = [
        'VacanciesPage'
    ]
    parent_page_types = ['EventIndexPage']

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


""" List of all events that have been created from events page """


class EventIndexPage(StandardPage):

    subpage_types = ['EventPage']

    def get_context(self,request):
        context = super().get_context(request)
    class Meta:
        verbose_name = "List of Events"
