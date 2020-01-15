from wagtail.core.blocks import (
    CharBlock, IntegerBlock, ListBlock, RichTextBlock, StructBlock, TextBlock)
from wagtail.snippets.blocks import SnippetChooserBlock


class IndicatorBlock(StructBlock):
    ddw_id = CharBlock(required=True, max_length=255, label='DDW ID')
    name = TextBlock(required=True)
    description = RichTextBlock(help_text='A description of this indicator')
    source = SnippetChooserBlock('spotlight.SpotlightSource')
    color = SnippetChooserBlock('spotlight.SpotlightColour')
    start_year = IntegerBlock()
    end_year = IntegerBlock()
    range = CharBlock(required=False, max_length=100)
    value_prefix = CharBlock(required=False, max_length=100)
    value_suffix = CharBlock(required=False, max_length=100)
    tooltip_template = TextBlock(required=True, help_text='Text for the tooltip.Template strings can be used to substitute values e.g. {name}')


class ThemeBlock(StructBlock):
    name = TextBlock(required=True)
    indicators = ListBlock(IndicatorBlock())
