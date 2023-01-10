from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.models import Orderable, Page
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet

from .constants import MAX_RELATED_LINKS

from typing import Dict


def hero_panels(allowed_pages=[]):
    """
    Called when creating page content_panels for pages that require a Hero
    Returns:
        MultiFieldPanel -- Hero content for a page
    """
    return MultiFieldPanel([
        FieldPanel('hero_image'),
        FieldPanel('hero_image_credit_name'),
        FieldPanel('hero_image_credit_url'),
        FieldPanel('hero_text', classname="hero_excerpt"),
        FieldPanel('hero_link_caption'),
        PageChooserPanel('hero_link', allowed_pages)
    ], heading="Hero Section")


def other_pages_panel():
    return MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')


def call_to_action_panel():
    return MultiFieldPanel([
        FieldPanel('call_to_action_title'),
        FieldPanel('call_to_action_body'),
        FieldPanel('call_to_action_button_text'),
        FieldPanel('call_to_action_button_url'),
    ], heading='Call to Action Section', classname='collapsible collapsed')


def get_paginator_range(paginator, page):
    """Return a 4 elements long list (two before and two after current page) containing a range of page numbers (int)."""
    range_start = max(page.number - 2, 1)
    range_end = min(page.number + 2, paginator.num_pages)
    return [i for i in range(range_start, range_end + 1)]


def get_related_pages(callingPage, selected_pages, queryset=None, min_len=MAX_RELATED_LINKS):
    count = len(selected_pages)

    if count < min_len:
        difference = min_len - count
        related_pages = [link.other_page if hasattr(link, 'other_page') else link for link in selected_pages]
        if related_pages and queryset:
            id_list = [page.id for page in related_pages if page]
            id_list.append(callingPage.id)
            if id_list:
                bonus_pages = []
                if isinstance(queryset, Dict):
                    for key in queryset:
                        results = queryset[key].live().exclude(id__in=id_list)
                        for item in results:
                            bonus_pages.append(item)
                else:
                    bonus_pages = queryset.live().exclude(id__in=id_list)
                return list(related_pages) + list(bonus_pages[:difference])
            return list(queryset.live()[:min_len])
        elif isinstance(queryset, Dict):
            bonus_pages = []
            for key in queryset:
                results = queryset[key].live().exclude(id=callingPage.id)
                for item in results:
                    bonus_pages.append(item)
            return list(bonus_pages[:min_len])
        elif queryset:
            return list(queryset.live().exclude(id=callingPage.id)[:min_len])

    order_related_pages_by_date = list([link.other_page if hasattr(link, 'other_page') else link for link in selected_pages])
    remove_blank_pages = list(filter(None, order_related_pages_by_date))
    pages_with_published_date = [d for d in remove_blank_pages if getattr(d.specific, 'published_date', 0) != 0 and d.specific.published_date]
    pages_with_published_date.sort(key=lambda x: x.specific.published_date, reverse=True)
    return pages_with_published_date

def multiple_email_validator(email_string):
    email_list = email_string.split(',')
    validator = EmailValidator()
    for email in email_list:
        try:
            validator(email)
        except ValidationError:
            raise ValidationError('"%s" is invalid' % email)


class PageNotification(models.Model):
    page = ParentalKey(Page, related_name='page_notifications', on_delete=models.CASCADE)

    date_time = models.DateTimeField(verbose_name='Notification date')
    title = models.CharField(
        max_length=255,
        verbose_name='Notification title',
        default='DI Website Scheduled Notification',
        help_text='This will be the subject of the notification email')
    message = RichTextField(
        verbose_name='Notification message',
        help_text='Body of the email. Supports tokens for page title (%page_title%) and page URL (%page_url%)')
    emails = models.TextField(
        help_text='Email addresses to notify. Multiple emails must be comma separated',
        validators=[multiple_email_validator])

    panels = [
        FieldPanel('date_time'),
        FieldPanel('title'),
        FieldPanel('message'),
        FieldPanel('emails')
    ]
