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

    class Meta():
        icon = 'fa-heart'


class BenefitsStreamBlock(StreamBlock):
    item = BenefitsBlock()
    required = False


class TeamStoryBlock(StructBlock):
    heading = TextBlock()
    subtitle_text = TextBlock()
    stories = StreamBlock([
        ('team_story_page', PageChooserBlock(required=False)),
    ])

    class Meta():
        icon = 'fa-book'


class TeamStoryStreamBlock(StreamBlock):
    item = TeamStoryBlock()
    required = False
