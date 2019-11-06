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
from wagtailgeowidget.blocks import GeoBlock

from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.blocks import ButtonBlock


class LocationsMapBlock(StructBlock):
    """
    Renders a map with all the DI office locations
    """
    heading = CharBlock(icon='fa-heading', required=False)
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


class FocusAreasBlock(StructBlock):
    """
    Renders the focus areas section
    """
    heading = CharBlock(icon='fa-heading', required=False, default='Our focus areas')
    focus_areas = ListBlock(TextBlock(icon='fa-text'), required=False)
    button = ButtonBlock()
    light = BooleanBlock(
        default=False,
        required=False,
        help_text='Applies a lighter background to the section')

    class Meta():
        icon = 'fa-list'
        template = 'blocks/focus_areas.html'


class ExpertiseBlock(StructBlock):
    """
    Renders the 'our expertise' section
    """
    heading = CharBlock(icon='fa-heading', required=False, default='Our expertise')
    description = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES,
        required=False)
    expertise_list = ListBlock(StructBlock([
        ('name', TextBlock(icon='fa-text')),
        ('description', RichTextBlock(
            icon='fa-paragraph',
            template='blocks/paragraph_block.html',
            features=RICHTEXT_FEATURES,
            required=False))
    ]), required=False)
    light = BooleanBlock(
        default=False,
        required=False,
        help_text='Applies a lighter background to the section')

    class Meta():
        template = 'blocks/expertise.html'


class MapBlock(StructBlock):
    """
    Allows the addition of a single benefit
    """
    location = TextBlock()
    address = TextBlock()
    map = GeoBlock()

    class Meta():
        icon = 'fa-map'


class MapStreamBlock(StreamBlock):
    """
    Handles creation of where we work locations
    """
    add_location = MapBlock()

    required = False
