import re

from django.core.exceptions import ValidationError
from django.forms import Media
from django.forms.utils import ErrorList
from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 ListBlock, PageChooserBlock, RichTextBlock,
                                 StreamBlock, StructBlock, TextBlock, URLBlock)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import (FOOTNOTE_RICHTEXT_FEATURES, RICHTEXT_FEATURES,
                                         RICHTEXT_FEATURES_NO_FOOTNOTES)
from di_website.publications.blocks import AudioMediaBlock
from di_website.publications.infographic import Infographic

class AccordionBlock(StructBlock):
    accordion_items = ListBlock(StructBlock([
    ('name', TextBlock(icon='heroicons-pencil-solid')),
    ('description', RichTextBlock(
            icon='heroicons-pencil-alt-solid',
            template='blocks/paragraph_block.html',
            features=RICHTEXT_FEATURES))
    ]))


    class Meta:
        template = 'blocks/accordion_block.html'

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
    section_sub_heading = RichTextBlock(required=False, features=RICHTEXT_FEATURES_NO_FOOTNOTES)
    document_box_heading = CharBlock(icon="title", required=False)
    document_boxes = StreamBlock([
        ('document_box', DocumentBoxBlock()),
    ], required=False)
    alt = BooleanBlock(default=True, help_text="White background if checked", required=False)


    class Meta:
        icon = 'doc-full-inverse'
        template = 'blocks/documentboxsection_block.html'


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """
    text = TextBlock()
    source = TextBlock(required=False, help_text='Who is this quote acredited to?')

    class Meta:
        icon = 'openquote'
        template = 'blocks/blockquote.html'


class SectionBlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """
    text = TextBlock()
    source = TextBlock(required=False, help_text='Who is this quote acredited to?')
    center = BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'openquote'
        template = 'blocks/section_blockquote.html'


class AbstractLinkBlock(StructBlock):
    caption = CharBlock(
        required=False,
        help_text='Leave blank if you wish to use the page title as a caption'
    )
    page = PageChooserBlock(
        required=False,
        help_text='For the link/button to show, either this or the url are required'
    )
    url = URLBlock(required=False, help_text='An alternative to an internal page')

    class Meta:
        icon = 'heroicons-link-solid'
        abstract = True


class LinkBlock(AbstractLinkBlock):
    class Meta:
        icon = 'heroicons-link-solid'
        template = 'blocks/link_block.html'


class ButtonBlock(AbstractLinkBlock):
    class Meta:
        template = 'blocks/button_block.html'
        label = 'A Link Button'
        form_classname = 'button-block indent-fields'
        help_text = 'Displays a link/button that navigates to the specified page or url when clicked'


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
    caption = CharBlock(
        required=False,
        help_text='Caption to appear beneath the image'
    )


class BannerBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    image_credit_name = TextBlock(required=False, help_text='The name of the image source')
    image_credit_url = URLBlock(required=False, help_text='A link to the image source, if any')
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='heroicons-video-camera-solid',
        template='blocks/embed_block.html',
        required=False
    )
    text = StreamBlock([
        ('text_heading', CharBlock(template='blocks/banner/text_heading.html', required=False, icon='title')),
        ('text', TextBlock(template='blocks/banner/text.html')),
        ('richtext', RichTextBlock(template='blocks/banner/richtext.html', features=RICHTEXT_FEATURES_NO_FOOTNOTES)),
        ('list', ListBlock(StructBlock([
            ('title', TextBlock(required=False, help_text='An optional title to the list item')),
            ('content', TextBlock(required=True, help_text='The list item content')),
        ], template='blocks/banner/list_item.html'), template='blocks/banner/list.html', icon='list-ul'))
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
        icon = 'heroicons-flag-solid'
        template = 'blocks/banner/banner_block.html'
        label = 'Banner Block'


class ContentBannerBlock(BannerBlock):
    class Meta():
        template = 'blocks/banner/content_banner_block.html'


class SectionParagraphBlock(StructBlock):
    text = RichTextBlock(features=RICHTEXT_FEATURES_NO_FOOTNOTES)
    center = BooleanBlock(default=False, required=False)

    class Meta():
        icon = 'heroicons-pencil-alt-solid'
        template = 'blocks/section_paragraph_block.html'


class AnchorBlock(StructBlock):
    anchor_id = CharBlock(required=True, help_text='The unique indentifier for this anchor')

    class Meta:
        icon = 'heroicons-badge-check-solid'
        template = 'blocks/anchor_block.html'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    paragraph_block = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
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
        icon = 'heroicons-photograph-solid'
        template = 'blocks/image_block.html'


class TestimonialBlock(StructBlock):
    body = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
    )
    cite = TextBlock(help_text='The source of the testimonial')
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'blocks/testimonial_block.html'


class AceEditorJSONBlock(StructBlock):
    """
    Renders the Ace Editor, allowing addition of JSON with limited intellisense
    """

    @property
    def media(self):
        return Media(
            js=[
                'https://cdnjs.cloudflare.com/ajax/libs/ace/1.11.2/ace.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/ace/1.11.2/theme-monokai.min.js'
            ]
        )

    content = TextBlock(
        label='JSON Content',
        help_text='Enter your JSON here',
        form_classname='ace-editor-json-block'
    )

    class Meta:
        form_classname = 'ace-editor-json-struct-block struct-block'


class AceEditorStreamBlock(StreamBlock):
    JSON = AceEditorJSONBlock()

    required = False


class CallToActionBlock(StructBlock):
    title = CharBlock(required=True, label='Title')
    body = TextBlock(
        required=False, label='Description',
        help_text='Optional: describe the purpose of your call to action in a bit more detail')
    button_text = CharBlock(
        required=False, label='Button Caption',
        help_text='Optional: this is required to show the button')
    button_url = URLBlock(
        required=False, label='Button URL',
        help_text='Optional: this is required to show the button')
    button_page = PageChooserBlock(
        required=False, label='Button Page',
        help_text='Optional: has priority over the button URL field')

    class Meta:
        icon = 'heroicons-flag-solid'
        label = 'Call To Action'
        template = 'blocks/call_to_action.html'

class TypesetStreamBlock(StreamBlock):
    """
    The custom blocks that can be used under an element with the typeset class (not sections)
    """
    anchor = AnchorBlock()
    paragraph_block = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        template='blocks/paragraph_block.html',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
    )
    block_quote = BlockQuote()
    button_block = ButtonBlock()
    link_block = LinkBlock()
    image = TypeSetImageBlock()
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='heroicons-video-camera-solid',
        template='blocks/embed_block.html',
        required=False
    )
    cta = CallToActionBlock()
    accordion = AccordionBlock()

    required = False


class BasicInfographicBlock(Infographic):
    class Meta:
        template = 'blocks/basic_infographic.html'


class Table(StructBlock):

    class Meta:
        help_text = 'Displays tabular data with an optional heading.'
        icon = 'list-ol'
        label = 'Table'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/table.html'

    heading = CharBlock(
        required=False
    )
    table = TableBlock()
    caption = RichTextBlock(
        required=False,
        features=FOOTNOTE_RICHTEXT_FEATURES,
        help_text='Optional: caption text to appear below the table'
    )
    caption_link = URLBlock(
        required=False,
        help_text='Optional: external link to appear below the table'
    )
    caption_label = CharBlock(
        required=False,
        help_text='Optional: label for the caption link, defaults to the link if left blank'
    )

class TypesetFootnoteStreamBlock(StreamBlock):
    """
    The custom blocks that can be used under an element with the typeset class (not sections)
    """
    anchor = AnchorBlock()
    paragraph_block = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        template='blocks/paragraph_block_footnote.html',
        features=RICHTEXT_FEATURES
    )
    block_quote = BlockQuote()
    button_block = ButtonBlock()
    link_block = LinkBlock()
    image = TypeSetImageBlock()
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='heroicons-video-camera-solid',
        template='blocks/embed_block.html',
        required=False
    )
    infographic = BasicInfographicBlock()
    cta = CallToActionBlock()
    table = Table()

    required = False



class MediaImageBlock(ImageBlock):
    class Meta:
        template = 'blocks/media_image_block.html'
        icon = 'heroicons-photograph-solid'


class ImageDuoTextBlock(ImageBlock):
    heading = CharBlock(icon='title', required=False)
    side_text = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES,
        template='blocks/paragraph_block.html',
        required=True
    )
    button = ButtonBlock()
    alt = BooleanBlock(default=False, help_text="White background if checked.", required=False)

    class Meta:
        template = 'blocks/duo_body_block_img.html'
        icon = 'heroicons-photograph-solid'


class FullWidthVideoBlock(StructBlock):
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        required=False
    )

    class Meta:
        template = 'blocks/full_width_embed.html'
        icon = 'heroicons-video-camera-solid'
        label = 'Full Width Video'


class CustomEmbedBlock(StructBlock):
    embed_type = ChoiceBlock(
        required=True,
        default='buzzsprout',
        choices=(
            ('buzzsprout', 'Buzzsprout'),
        )
    )
    embed_url = URLBlock(required=True, help_text='The URL contained within the embed provider source code.')

    class Meta:
        template = 'blocks/custom_embed.html'
        icon = 'heroicons-adjustments-solid'
        label = 'Custom Embed'

    def clean(self, value):
        errors = {}

        if value.get('embed_type') == 'buzzsprout':
            buzzsprout_regex = r'^https:\/\/www\.buzzsprout\.com\/.+container_id.+$'
            pattern = re.compile(buzzsprout_regex)
            match = re.match(pattern, value.get('embed_url'))
            if match is None:
                errors['embed_url'] = ErrorList(['Please enter a valid Buzzsprout embed URL.'])

        if errors:
            raise ValidationError('Validation error in StructBlock', params=errors)

        return super().clean(value)


class VideoDuoTextBlock(StructBlock):
    heading = CharBlock(icon='title', required=False, help_text='Section heading')
    video = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='heroicons-video-camera-solid',
        template='blocks/embed_block.html',
        required=False
    )
    side_text = RichTextBlock(
        icon='heroicons-pencil-alt-solid',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES,
        template='blocks/paragraph_block.html',
        required=True
    )
    button = ButtonBlock()
    alt = BooleanBlock(default=False, help_text="White background if checked.", required=False)

    class Meta:
        template = 'blocks/duo_body_block_vid.html'
        icon = 'heroicons-video-camera-solid'


class SectionStreamBlock(StreamBlock):
    """
    The custom blocks that can be rendered as independent sections on a page
    """
    anchor = AnchorBlock()
    paragraph_block = SectionParagraphBlock()
    block_quote = SectionBlockQuote()
    banner_block = BannerBlock()
    downloads = DocumentBoxSectionBlock()
    image = MediaImageBlock()
    image_duo = ImageDuoTextBlock()
    audio_block = AudioMediaBlock(max_num=1)
    video_duo = VideoDuoTextBlock()
    full_width_video_block = FullWidthVideoBlock()
    custom_embed = CustomEmbedBlock()
    cta = CallToActionBlock(template='blocks/section_call_to_action.html')
    accordion = AccordionBlock()

    required = False
