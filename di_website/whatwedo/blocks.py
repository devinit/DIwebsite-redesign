from wagtail.blocks import (
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

from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES
from di_website.common.blocks import ButtonBlock


class LocationsMapBlock(StructBlock):
    """
    Renders a map with all the DI office locations
    """
    heading = CharBlock(icon='title', required=False)
    description = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES,
        required=False)
    button = ButtonBlock()
    light = BooleanBlock(
        default=False,
        required=False,
        help_text='Applies a lighter background to the section')

    class Meta():
        icon = 'heroicons-location-marker-solid'
        template = 'blocks/locations_map.html'


class FocusAreasBlock(StructBlock):
    """
    Renders the focus areas section
    """
    heading = CharBlock(icon='title', required=False, default='Our focus areas')
    focus_areas = ListBlock(TextBlock(icon='heroicons-pencil-solid'), required=False)
    button = ButtonBlock()
    light = BooleanBlock(
        default=False,
        required=False,
        help_text='Applies a lighter background to the section')

    class Meta():
        icon = 'heroicons-list-ul-solid'
        template = 'blocks/focus_areas.html'


class ExpertiseBlock(StructBlock):
    """
    Renders the 'our expertise' section
    """
    heading = CharBlock(icon='title', required=False, default='Our expertise')
    description = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES,
        required=False)
    expertise_list = ListBlock(StructBlock([
        ('name', TextBlock(icon='heroicons-pencil-solid')),
        ('description', RichTextBlock(
            icon='heroicons-pencil-alt-solid',
            template='blocks/paragraph_block.html',
            features=RICHTEXT_FEATURES_NO_FOOTNOTES,
            required=False))
    ]), required=False)
    light = BooleanBlock(
        default=False,
        required=False,
        help_text='Applies a lighter background to the section')

    class Meta():
        template = 'blocks/expertise.html'


class WhereWeWorkLocationBlock(StructBlock):
    """
    Allows the addition of a single where we work location
    """
    name = TextBlock()
    phone = TextBlock(required=False)
    google_map = GeoBlock()

    class Meta():
        icon = 'heroicons-map-solid'


class MapStreamBlock(StreamBlock):
    """
    Handles creation of where we work locations
    """
    location = WhereWeWorkLocationBlock(label='Add Location')
