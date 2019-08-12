from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock
)
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.blocks import LinkBlock


class PlaceBlock(StructBlock):
    title = TextBlock()
    subtitle = TextBlock(required=False)
    image = ImageChooserBlock(required=False)
    body = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES
    )
    side_section_title = TextBlock(required=False)
    links = StreamBlock([('link', LinkBlock())], required=False)

    class Meta():
        icon = 'fa-globe'
        template = 'blocks/place_block.html'


class PlaceStreamBlock(StreamBlock):
    place = PlaceBlock()
    required = False
