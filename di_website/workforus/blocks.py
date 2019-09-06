from django.db import models

from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.blocks import LinkBlock


class BenefitsBlock(StructBlock):
    title = TextBlock()
    body = RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    logos = StreamBlock([
        ('image', ImageChooserBlock()),
    ])

    class Meta():
        icon = 'fa-heart'


class BenefitsStreamBlock(StreamBlock):
    item = BenefitsBlock()
    required = False


class TeamStoryBlock(StructBlock):
    title = TextBlock()
    story_url = URLBlock()
    image = ImageChooserBlock(required=False)

    class Meta():
        icon = 'fa-book'


class TeamStoryStreamBlock(StreamBlock):
    item = TeamStoryBlock()
    required = False
