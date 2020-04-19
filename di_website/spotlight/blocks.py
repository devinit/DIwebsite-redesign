from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    CharBlock,
    ChoiceBlock
)

from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES


class CountryInfoStreamBlock(StreamBlock):
    country_info = StreamBlock([
        ('add_spotlight_page', PageChooserBlock(required=False, target_model='spotlight.SpotlightPage')),
    ],
        blank=True,
        max_num=2,
        block_counts={
            'add_spotlight_page': {'max_num': 2},
        }
    )
    required = False
