from django.db import models

from di_website.common.mixins import HeroMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.common.base import hero_panels

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    InlinePanel,
    PageChooserPanel,
)

from wagtail.core.fields import StreamField
from wagtail.core.models import Page


class General(TypesetBodyMixin, HeroMixin, SectionBodyMixin, Page):

    """
    General page that that can be used with strategy  and accounts pages
    """

    template = 'general/general_page.html'

    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )
    show_breadcrumbs = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('show_breadcrumbs'),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    class Meta:
        verbose_name = 'General Page'
