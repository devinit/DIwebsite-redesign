from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    CharBlock,
    ChoiceBlock
)

from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES


class CountryInfoBlock(StructBlock):
    title = CharBlock()
    spotlight_description = StreamBlock([
        ('description', RichTextBlock(
            icon='fa-paragraph',
            template='blocks/paragraph_block.html',
            features=RICHTEXT_FEATURES_NO_FOOTNOTES
        ))
    ], blank=True, max_num=2)
    spotlight_page = StreamBlock([
        ('add_spotlight_page', PageChooserBlock(required=False, target_model='spotlight.SpotlightPage')),
        ('add_location_comparison_page', PageChooserBlock(required=False, target_model='spotlight.SpotlightLocationComparisonPage'))
    ],
        blank=True,
        max_num=2,
        block_counts={
            'add_spotlight_page': {'max_num': 1},
            'add_location_comparison_page': {'max_num': 1}
        }
    )
    background_theme = ChoiceBlock(choices=[
        ('light', 'Light'),
        ('dark', 'Dark'),
    ], help_text='Select background theme for this section')

    class Meta():
        icon = 'fa-globe'


class CountryInfoStreamBlock(StreamBlock):
    country_info = CountryInfoBlock()
    required = False
