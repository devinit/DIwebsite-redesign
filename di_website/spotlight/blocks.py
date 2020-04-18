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
    spotlight_page = StreamBlock([
        ('add_spotlight_page', PageChooserBlock(required=False, target_model='spotlight.SpotlightPage')),
    ],
        blank=True,
        max_num=2,
        block_counts={
            'add_spotlight_page': {'max_num': 2},
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
