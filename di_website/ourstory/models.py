from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.base import hero_panels
from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin


class OurStoryPage(BaseStreamBodyMixin, HeroMixin, Page):

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body')
    ]

    class Meta():
        verbose_name = 'Our Story Page'
