from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
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
        icon = 'fa-quote-left'
        template = 'blocks/blockquote.html'


class ParagraphBlock(StructBlock):
    text = RichTextBlock(
        icon='fa-paragraph',
        features=RICHTEXT_FEATURES
    )
    is_typeset = BooleanBlock(required=False)
    is_section = BooleanBlock(required=False)
    classname = CharBlock(
        required=False,
        help_text='e.g. vacancy pages have a "is-typeset--additionals" class that customises particular areas'
    )

    class Meta():
        template = 'blocks/paragraph_block.html'
        icon="fa-paragraph"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    paragraph_block = ParagraphBlock()
    block_quote = BlockQuote()
