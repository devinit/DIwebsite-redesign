from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import (
    CharBlock,
    RichTextBlock,
    StructBlock,
    StreamBlock,
)
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.base import hero_panels
from di_website.common.blocks import DocumentBoxBlock, BaseStreamBlock, ValueBlock
from di_website.common.mixins import HeroMixin, SectionBodyMixin, TypesetBodyMixin


class TimelineItemBlock(StructBlock):
    month = CharBlock(required=False, help_text="Month abbreviation E.g. Apr")
    year = CharBlock(required=False, help_text="Year E.g. 2008")
    title = CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    text = RichTextBlock(required=False)
    documents = DocumentBoxBlock(required=False)


class TimelineCarouselStreamBlock(StreamBlock):
    item = TimelineItemBlock()
    required = False

    class Meta():
        template = 'blocks/timeline_carousel.html'


class OurStoryPage(SectionBodyMixin, TypesetBodyMixin, HeroMixin, Page):

    timeline_items = StreamField(TimelineCarouselStreamBlock)
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('timeline_items'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')
    ]

    class Meta():
        verbose_name = 'Our Story Page'

    subpage_types = ['general.General']
    parent_page_types = ['WhoWeArePage']


class WhoWeArePage(SectionBodyMixin, TypesetBodyMixin, HeroMixin, Page):
    subpage_types = ['OurStoryPage', 'general.General', 'ourteam.OurTeamPage']

    value_section_heading = models.CharField(blank=True, max_length=255)
    value_section_sub_heading = models.TextField(blank=True)
    values = StreamField([
        ('value', ValueBlock()),
    ], null=True, blank=True)

    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections'),
        FieldPanel('value_section_heading'),
        FieldPanel('value_section_sub_heading'),
        StreamFieldPanel('values'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')
    ]

    class Meta():
        verbose_name = 'Who We Are Page'

    subpage_types = ['general.General']
