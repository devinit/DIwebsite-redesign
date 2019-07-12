from wagtail.core.blocks import (
    StructBlock,
    TextBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)

from di_website.common.constants import RICHTEXT_FEATURES


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """
    text = TextBlock()

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="blocks/paragraph_block.html",
        features=RICHTEXT_FEATURES
    )
    block_quote = BlockQuote()
