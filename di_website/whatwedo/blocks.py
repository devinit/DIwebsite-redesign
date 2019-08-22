from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DecimalBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.blocks import ButtonBlock


class LocationsMapBlock(StructBlock):
    """
    Renders a map with all the DI office locations
    """
    heading = CharBlock(icon="fa-heading", required=False)
    description = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES,
        required=False)
    button = ButtonBlock()
    light = BooleanBlock(
        default=False,
        required=False,
        help_text='Applies a lighter background to the section')

    class Meta():
        icon = 'fa-map-marker'
        template = 'blocks/locations_map.html'
