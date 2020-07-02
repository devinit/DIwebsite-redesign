from wagtail.core.fields import StreamField
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.snippets.blocks import SnippetChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES, RICHTEXT_FEATURES_NO_FOOTNOTES, FOOTNOTE_RICHTEXT_FEATURES
from .infographic import PublicationInfographic
from di_website.common.blocks import AnchorBlock


class CaptionedImage(StructBlock):

    class Meta:
        help_text = 'Displays an image with an optionally linked caption.'
        icon = 'image'
        label = 'Captioned image'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/captioned_image.html'

    image = ImageChooserBlock(
        help_text='Optimal minimum width 800px'
    )
    descriptive_text = RichTextBlock(
        required=False,
        features=FOOTNOTE_RICHTEXT_FEATURES,
        help_text='Optional: descriptive text to appear above the image'
    )
    caption = TextBlock(
        required=False,
        help_text='Optional: caption text to appear below the image'
    )
    caption_link = URLBlock(
        required=False,
        help_text='Optional: external link to appear below the image'
    )
    caption_label = CharBlock(
        required=False,
        help_text='Optional: label for the caption link, defaults to the link if left blank'
    )


class CaseStudy(StructBlock):

    class Meta:
        help_text = 'Displays a case study with a heading, and at least one block of WYSIWYG content, infographic, or captioned image.'
        icon = 'doc-full'
        label = 'Case study'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/case_study.html'

    section_label = CharBlock(default="Case Study")
    heading = CharBlock()
    content = StreamBlock(
        [
            ('rich_text', RichTextBlock(
                required=False,
                features=RICHTEXT_FEATURES,
                label='WYSIWYG editor',
            )),
            ('infographic', PublicationInfographic(
                required=False,
            )),
            ('captioned_image', CaptionedImage(
                required=False,
            )),
        ],
    )


class DefinitionList(StructBlock):

    class Meta:
        help_text = 'Displays a list of terms and definitions.'
        icon = 'list-ul'
        label = 'Definition list'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/definition_list.html'

    definitions = ListBlock(
        StructBlock([
            ('term', CharBlock()),
            ('definition', TextBlock()),
        ]),
        icon='list-ul'
    )


class Downloads(StructBlock):

    class Meta:
        help_text = 'Displays a list of file downloads or external URLs.'
        icon = 'list-ul'
        label = 'Download list'
        form_template = 'publications/block_forms/custom_struct.html'
        form_classname = 'custom__itemlist struct-block'
        template = 'publications/blocks/downloads.html'

    downloads = StreamBlock(
        [
            ('file', StructBlock(
                [
                    ('file', SnippetChooserBlock('downloads.PublicationDownload')),
                ],
                icon='doc-empty',
                label='File'
            )),
            ('url', StructBlock(
                [
                    ('label', CharBlock()),
                    ('url', URLBlock()),
                ],
                icon='site',
                label='URL'
            )),
        ],
    )


class SectionHeading(StructBlock):

    class Meta:
        help_text = 'Displays a heading for a content section.'
        icon = 'title'
        label = 'Section heading'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/section_heading.html'

    section_id = CharBlock(
        help_text='Prepended by a chapter number if available, this value should be unique to the page, e.g. "1", "1.1", "2", "2.1" etc.'
    )
    heading = CharBlock()


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


class AbstractRichText(StructBlock):

    class Meta:
        abstract = True
        help_text = 'Displays rich text content edited via a WYSIWYG editor'
        icon = 'doc-full'
        label = 'WYSIWYG editor'
        form_template = 'publications/block_forms/custom_struct.html'


class RichText(AbstractRichText):

    class Meta:
        template = 'publications/blocks/rich_text.html'

    rich_text = RichTextBlock(
        features=RICHTEXT_FEATURES,
    )


class RichTextNoFootnotes(AbstractRichText):

    class Meta:
        template = 'publications/blocks/rich_text_no_footnotes.html'

    rich_text = RichTextBlock(
        features=RICHTEXT_FEATURES_NO_FOOTNOTES,
    )


def flexible_content_streamfield(blank=False):
    return StreamField([
        ('captioned_image', CaptionedImage()),
        ('case_study', CaseStudy()),
        ('definition_list', DefinitionList()),
        ('downloads', Downloads()),
        ('section_heading', SectionHeading()),
        ('table', Table()),
        ('rich_text', RichText()),
        ('infographic', PublicationInfographic()),
        ('anchor', AnchorBlock()),
    ], blank=blank)


def content_streamfield(blank=False):
    return StreamField([
        ('captioned_image', CaptionedImage()),
        ('definition_list', DefinitionList()),
        ('table', Table()),
        ('rich_text', RichTextNoFootnotes()),
        ('anchor', AnchorBlock()),
    ], blank=blank)
