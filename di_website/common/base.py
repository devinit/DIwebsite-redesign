from django.db import models
from django.utils.functional import cached_property

from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey

from .blocks import BaseStreamBlock


class StandardPage(Page):
    """
    StandardPage contains properties that are shared across multiple pages
    """
    class Meta:
        abstract = True

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Hero Image'
    )
    hero_image_credit_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Image credit name',
        help_text='Name of source of image used in hero if any'
    )
    hero_image_credit_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image credit url',
        help_text='A Link to the original source of the image if any'
    )
    hero_text = RichTextField(
        null=True,
        blank=True,
        help_text='A description of the page content'
    )
    hero_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero link',
        help_text='Choose a page to link to for the Call to Action'
    )
    hero_link_caption = models.CharField(
        max_length=255,
        blank=True,
        help_text='Text to display on the link button'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            FieldPanel('hero_image_credit_name'),
            FieldPanel('hero_image_credit_url'),
            FieldPanel('hero_text', classname="hero_excerpt"),
            FieldPanel('hero_link_caption'),
            PageChooserPanel('hero_link')
        ], heading="Hero Section"),
    ]


class OtherPage(Orderable, models.Model):
    page = ParentalKey(
        Page, related_name='other_pages', on_delete=models.CASCADE
    )

    other_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Other Page',
        help_text='Choose a page to link to in the "Other Pages" section'
    )

    class Meta():
        abstract = True


class BaseStreamBody(models.Model):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

class BaseDownload(models.Model):
    class Meta:
        abstract = True

    page = ParentalKey(
        Page, related_name='page_downloads', on_delete=models.CASCADE
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: document title, defaults to the file name if left blank',
    )

    @cached_property
    def get_title(self):
        return self.title if self.title else self.file.title

    def __str__(self):
        return self.title if self.title else self.file.title


@register_snippet
class Download(BaseDownload):
    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title')
    ]


def get_paginator_range(paginator, page):
    """Return a 3 elements long list containing a range of page numbers (int)."""
    range_start = max(page.number - 3, 1)
    range_end = min(page.number + 2, paginator.num_pages)
    return [i for i in range(range_start, range_end + 1)]
