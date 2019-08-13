from wagtail.admin.edit_handlers import StreamFieldPanel
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
from di_website.common.blocks import DocumentBoxBlock, BaseStreamBlock
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin


class TimelineItemBlock(StructBlock):
    month = CharBlock(required=False, help_text="Month abbreviation E.g. Apr")
    year = CharBlock(required=False, help_text="Year E.g. 2008")
    title = CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    text = RichTextBlock(required=False)
    documents = DocumentBoxBlock(required=False)


class TimelineCarouselStreamBlock(StreamBlock):
    items = TimelineItemBlock()
    required = False

    class Meta():
        template = 'blocks/timeline_carousel.html'


class OurStoryPage(BaseStreamBodyMixin, HeroMixin, Page):

    timeline_items = StreamField(TimelineCarouselStreamBlock)
    post_carousel_body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('timeline_items'),
        StreamFieldPanel('post_carousel_body'),
    ]

    class Meta():
        verbose_name = 'Our Story Page'
