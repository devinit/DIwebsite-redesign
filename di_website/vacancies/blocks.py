from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)

from di_website.common.blocks import BlockQuote
from di_website.common.constants import RICHTEXT_FEATURES


# StreamBlocks
class VacancyStreamBlock(StreamBlock):
    """
    Define the custom blocks that the vacancy body `StreamField` will utilize
    """
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="blocks/paragraph_block.html",
        features=RICHTEXT_FEATURES
    )
    block_quote = BlockQuote()
