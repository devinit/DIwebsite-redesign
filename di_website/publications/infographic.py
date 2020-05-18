from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    StructValue,
    TextBlock,
    URLBlock,
)
from wagtail.snippets.blocks import SnippetChooserBlock
from di_website.common.constants import FOOTNOTE_RICHTEXT_FEATURES

HELP_TEXT = '''Content to display an infographic at wide screen widths, and optionally at medium and narrow screen widths. </br>
            A long description and/or tabular data is required to support the graphic. </br>
            Optional caption and download links display below the image/data.'''


class InfographicStructValue(StructValue):

    def has_narrow(self):
        for image in self.get('images'):
            if image.block_type == 'image_narrow':
                if image.value.get('narrow') or image.value.get('use_next_widest_image'):
                    return True
        return False

    def has_medium(self):
        for image in self.get('images'):
            if image.block_type == 'image_medium':
                if image.value.get('medium') or image.value.get('use_wide_image'):
                    return True
        return False

    def wide_image(self):
        for image in self.get('images'):
            if image.block_type == 'image_wide':
                return image.value.get('wide')
        return ''

    def has_downloads(self):
        if self.get('caption_link'):
            return True
        for item in self.get('downloads'):
            if item:
                return True
        return False


class Infographic(StructBlock):

    class Meta:
        help_text = HELP_TEXT
        value_class = InfographicStructValue
        icon = 'form'
        label = 'Infographic'
        form_classname = 'custom__itemlist struct-block'
        form_template = 'publications/block_forms/custom_struct.html'
        abstract = True

    heading = CharBlock(
        required=False,
        help_text='Optional: heading for the infographic'
    )
    descriptive_text = RichTextBlock(
        required=False,
        features=FOOTNOTE_RICHTEXT_FEATURES,
        help_text='Optional: descriptive text to appear above the image or table'
    )
    images = StreamBlock(
        [
            ('image_wide', StructBlock(
                [
                    ('wide', ImageChooserBlock(
                        help_text='Optimal minimum width 2400px'
                    )),
                ],
                icon='image',
                label='Wide',
                form_template='publications/block_forms/custom_struct.html',
                help_text='<b>Note:</b> infographics always require a wide image. Medium and narrow images are optional.'
            )),
            ('image_medium', StructBlock(
                [
                    ('medium', ImageChooserBlock(
                        required=False,
                        help_text='Optional: optimal minimum width 1560px'
                    )),
                    ('use_wide_image', BooleanBlock(
                        required=False,
                        help_text='Optional: check this box to display the wide image at medium viewport sizes'
                    )),
                ],
                icon='image',
                label='Medium',
            )),
            ('image_narrow', StructBlock(
                [
                    ('narrow', ImageChooserBlock(
                        required=False,
                        help_text='Optional: optimal minimum width 1000px'
                    )),
                    ('use_next_widest_image', BooleanBlock(
                        required=False,
                        help_text='Optional: check this box to display the next widest image at narrow viewport sizes (if available)'
                    )),
                ],
                icon='image',
                label='Narrow',
            )),
        ],
        min_num=1,
        max_num=3,
        block_counts={
            'image_wide': {
                'min_num': 1,
                'max_num': 1
            },
            'image_medium': {
                'max_num': 1
            },
            'image_narrow': {
                'max_num': 1
            },
        },
    )
    data = StreamBlock(
        [
            ('long_description', StructBlock(
                [
                    ('long_description', TextBlock(
                        help_text='Infographics require a long description and/or tabular data'
                    )),
                ],
                icon='bold',
                label='Long desc',
            )),
            ('table', StructBlock(
                [
                    ('table', TableBlock(
                        help_text='Infographics require a long description and/or tabular data'
                    )),
                ],
                icon='list-ol',
                label='Table',
            )),
        ],
        min_num=1,
        max_num=2,
        block_counts={
            'table': {
                'max_num': 1
            },
            'long_description': {
                'max_num': 1
            }
        },
    )
    caption = RichTextBlock(
        required=False,
        features=FOOTNOTE_RICHTEXT_FEATURES,
        help_text='Optional: caption text to appear below the image or table'
    )
    caption_link = URLBlock(
        required=False,
        help_text='Optional: external link to appear below the image or table'
    )
    caption_label = CharBlock(
        required=False,
        help_text='Optional: label for the caption link, defaults to the link if left blank'
    )
    downloads = ListBlock(
        SnippetChooserBlock('downloads.PublicationDownload', required=False),
        help_text='Optional: list of downloads to appear below the image or table'
    )


class PublicationInfographic(Infographic):
    class Meta:
        template = 'publications/blocks/infographic.html'
