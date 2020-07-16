from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock)
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES


class BenefitBlock(StructBlock):
    """
    Allows the addition of a single benefit
    """
    title = TextBlock()
    body = RichTextBlock(required=False, features=RICHTEXT_FEATURES_NO_FOOTNOTES)
    image = ImageChooserBlock(required=False)

    class Meta():
        icon = 'fa-heart'


class BenefitsStreamBlock(StreamBlock):
    """
    Handles the benefits section of the 'Work for Us' page
    """
    benefit = BenefitBlock()
    logo = ImageChooserBlock(required=False)

    required = False


class TeamStoryBlock(StructBlock):
    team_story_page = PageChooserBlock(
        verbose_name='Story Page',
        page_type=['general.General']
    )
    logo = ImageChooserBlock()

    class Meta():
        icon = 'fa-book'
        verbose_name = 'Team Story'


class TeamStoryStreamBlock(StreamBlock):
    team_story = TeamStoryBlock()
    required = False
