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


class SectionBlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """
    text = TextBlock()
    center = BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'fa-quote-right'
        template = 'blocks/section_blockquote.html'


class LinkBlock(StructBlock):
    caption = CharBlock(required=False)
    url = URLBlock(required=False)
    page = PageChooserBlock(required=False)


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
    buttons = StreamBlock([('button', LinkBlock())], required=False)

    class Meta():
        icon = 'fa-flag'
        template = 'blocks/banner_block.html'


class SectionParagraphBlock(StructBlock):
    text = RichTextBlock(features=RICHTEXT_FEATURES)
    center = BooleanBlock(default=False, required=False)

    class Meta():
        icon = 'fa-paragraph'
        template = 'blocks/section_paragraph_block.html'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    paragraph_block = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES
    )
    section_paragraph_block = SectionParagraphBlock()
    block_quote = BlockQuote()
    section_block_quote = SectionBlockQuote()
    banner_block = BannerBlock()
    required = False
