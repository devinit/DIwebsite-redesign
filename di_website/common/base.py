from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from .constants import MAX_RELATED_LINKS


def hero_panels(allowed_pages=[]):
    """
    Called when creating page content_panels for pages that require a Hero
    Returns:
        MultiFieldPanel -- Hero content for a page
    """
    return MultiFieldPanel([
        ImageChooserPanel('hero_image'),
        FieldPanel('hero_image_credit_name'),
        FieldPanel('hero_image_credit_url'),
        FieldPanel('hero_text', classname="hero_excerpt"),
        FieldPanel('hero_link_caption'),
        PageChooserPanel('hero_link', allowed_pages)
    ], heading="Hero Section")


def get_paginator_range(paginator, page):
    """Return a 4 elements long list (two before and two after current page) containing a range of page numbers (int)."""
    range_start = max(page.number - 2, 1)
    range_end = min(page.number + 2, paginator.num_pages)
    return [i for i in range(range_start, range_end + 1)]


def get_related_pages(selected_pages, queryset=None, min_len=MAX_RELATED_LINKS):
    count = len(selected_pages)

    if count < min_len:
        difference = min_len - count
        related_pages = [link.other_page for link in selected_pages]
        if related_pages and queryset:
            id_list = [page.id for page in related_pages if page]
            if id_list:
                return list(related_pages) + list(queryset.live().exclude(id__in=id_list)[:difference])
            return list(queryset.live()[:min_len])
        elif queryset:
            return list(queryset.live()[:min_len])

    return list([link.other_page for link in selected_pages])


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
