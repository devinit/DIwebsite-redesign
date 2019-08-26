from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DecimalBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES


class ValueBlock(StructBlock):
    """
    A block for holding a single value.
    """

    title = CharBlock(icon="title", required=False)
    excerpt = TextBlock(required=False)

    class Meta:
        template = 'blocks/value_block.html'


class DocumentBoxBlock(StructBlock):
    """
    A block for holding a document box, with a single header and multiple documents.
    """

    box_heading = CharBlock(icon="title", required=False)
    documents = StreamBlock([
        ('document', DocumentChooserBlock()),
    ], required=False)
    dark_mode = BooleanBlock(
        default=False,
        required=False,
        help_text="Red on white if unchecked. White on dark grey if checked."
    )

    DocumentChooserBlock(icon="doc-full-inverse", required=False)

    class Meta:
        icon = 'doc-full-inverse'
        template = 'blocks/documentbox_block.html'


class DocumentBoxSectionBlock(StructBlock):
    """
    A block for holding multiple document boxes.
    """
    section_heading = TextBlock(required=False)
    section_sub_heading = TextBlock(required=False)
    document_box_heading = CharBlock(icon="title", required=False)
    document_boxes = StreamBlock([
        ('document_box', DocumentBoxBlock()),
    ], required=False)


    class Meta:
        icon = 'doc-full-inverse'
        template = 'blocks/documentboxsection_block.html'


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


class AbstractLinkBlock(StructBlock):
    caption = CharBlock(required=False)
    url = URLBlock(required=False)
    page = PageChooserBlock(required=False)

    class Meta:
        icon = 'fa-link'
        abstract = True


class LinkBlock(AbstractLinkBlock):
    class Meta:
        icon = 'fa-link'
        template = 'blocks/link_block.html'


class ButtonBlock(AbstractLinkBlock):
    class Meta:
        icon = 'fa-link'
        template = 'blocks/button_block.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    credit_name = CharBlock(
        required=False,
        help_text='Name of the image source'
    )
    credit_url = URLBlock(
        required=False,
        help_text='URL of the image source'
    )


class BannerBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-s15',
        template='blocks/embed_block.html',
        required=False
    )
    text = StreamBlock([
        ('text', TextBlock(template='blocks/banner/text.html')),
        ('list', ListBlock(StructBlock([
            ('title', TextBlock()),
            ('content', TextBlock(required=False)),
        ], template='blocks/banner/list_item.html'), template='blocks/banner/list.html'))
    ])
    meta = CharBlock(
        required=False,
        help_text='Anything from a name, location e.t.c - usually to provide credit for the text'
    )
    buttons = StreamBlock([
        ('button', LinkBlock()),
        ('document_box', DocumentBoxBlock())
    ], required=False)
    media_orientation = ChoiceBlock(
        required=False,
        default='left',
        choices=(
            ('left', 'Left'),
            ('right', 'Right'),
        )
    )
    light = BooleanBlock(
        required=False, default=False, help_text='Sets the background to a lighter colour')

    class Meta():
        icon = 'fa-flag'
        template = 'blocks/banner/banner_block.html'


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
    button_block = ButtonBlock()
    link_block = LinkBlock()
    required = False


class TypeSetImageBlock(ImageBlock):
    class Meta:
        icon = 'fa-image'
        template = 'blocks/image_block.html'

class TypesetStreamBlock(StreamBlock):
    """
    The custom blocks that can be used under an element with the typeset class (not sections)
    """
    paragraph_block = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES
    )
    block_quote = BlockQuote()
    button_block = ButtonBlock()
    link_block = LinkBlock()
    image = TypeSetImageBlock()

    required = False


class SectionStreamBlock(StreamBlock):
    """
    The custom blocks that can be rendered as independent sections on a page
    """
    paragraph_block = SectionParagraphBlock()
    block_quote = SectionBlockQuote()
    banner_block = BannerBlock()

    required = False

class MediaImageBlock(ImageBlock):
    class Meta:
        template = 'blocks/media_image_block.html'


class ImageDuoTextBlock(ImageBlock):
    side_text = RichTextBlock(
        icon='fa-paragraph',
        features=RICHTEXT_FEATURES,
        template='blocks/paragraph_block.html',
        required=True
    )
    class Meta:
        template = 'blocks/duo_body_block_img.html'


class VideoDuoTextBlock(StructBlock):
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-video-camera',
        template='blocks/embed_block.html',
        required=False
    )
    side_text = RichTextBlock(
        icon='fa-paragraph',
        features=RICHTEXT_FEATURES,
        template='blocks/paragraph_block.html',
        required=True
    )
    class Meta:
        template = 'blocks/duo_body_block_vid.html'


class DuoContentStreamBlock(StreamBlock):
    """
    Displays with video or image aligned to left with text aligned to the right
    """
    image_block = ImageDuoTextBlock()
    video_block = VideoDuoTextBlock()
    media_image = MediaImageBlock()
    text_block = SectionParagraphBlock()


    required = False
