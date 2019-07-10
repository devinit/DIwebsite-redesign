from wagtail.core.blocks import (
    StructBlock,
    TextBlock,
)


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """
    text = TextBlock()

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"
