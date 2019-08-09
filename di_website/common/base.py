from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .mixins import BaseDownloadMixin


def hero_panels():
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
        PageChooserPanel('hero_link')
    ], heading="Hero Section")


@register_snippet
class Download(BaseDownloadMixin):
    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title')
    ]


def get_paginator_range(paginator, page):
    """Return a 4 elements long list (two before and two after current page) containing a range of page numbers (int)."""
    range_start = max(page.number - 2, 1)
    range_end = min(page.number + 2, paginator.num_pages)
    return [i for i in range(range_start, range_end + 1)]
