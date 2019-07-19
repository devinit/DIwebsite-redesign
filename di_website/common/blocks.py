from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

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


class BannerBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-s15',
        template='blocks/embed_block.html',
        required=False
    )
    text = TextBlock()
    meta = CharBlock(
        required=False,
        help_text='Anything from a name, location e.t.c - usually to provide credit for the text'
    )
    button_caption = CharBlock(required=False)
    button_link = URLBlock(required=False)
    button_page = PageChooserBlock(required=False)
    is_section = BooleanBlock(required=False, default=False)

    class Meta():
        icon = 'fa-flag'
        template = 'blocks/banner_block.html'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    paragraph_block = ParagraphBlock()
    block_quote = BlockQuote()
    banner_block = BannerBlock()
    required = False
