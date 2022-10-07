from wagtail.blocks.field_block import BooleanBlock
from wagtail.fields import StreamField
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import (
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
    PageChooserBlock
)
from wagtail.snippets.blocks import SnippetChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES, RICHTEXT_FEATURES_NO_FOOTNOTES, FOOTNOTE_RICHTEXT_FEATURES
from .infographic import PublicationInfographic
from di_website.common.blocks import AccordionBlock, AnchorBlock, CallToActionBlock, SectionBlockQuote


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


class PivotTable(StructBlock):

    class Meta:
        help_text = 'Uses a CSV data source to displays tabular data with an optional title.'
        icon = 'table'
        label = 'Pivot Table'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/pivot-table.html'

    show_title = BooleanBlock(required=False, default=True)
    pivot_table = PageChooserBlock(page_type=['visualisation.PivotTable'])

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        pivot_table = value['pivot_table']
        context['table'] = pivot_table.specific if pivot_table and pivot_table.live else ''
        return context

class DynamicTable(StructBlock):

    class Meta:
        help_text = 'Uses a CSV data source to display tabular data with an optional heading.'
        icon = 'table'
        label = 'Dynamic Table'
        form_template = 'publications/block_forms/custom_struct.html'
        template = 'publications/blocks/dynamic-table.html'

    heading = CharBlock(
        required=False
    )
    data_source_url = URLBlock(help_text='Link to the CSV data file')
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


class InteractiveChartBlock(StructBlock):

    class Meta:
        help_text = 'Select a Plotly Studio chart page'
        icon = 'fa-area-chart'
        label = 'Plotly Studio Chart'
        template = 'publications/blocks/interactive_chart.html'
        form_template = 'publications/block_forms/custom_struct.html'

    chart_page = PageChooserBlock(
        page_type='visualisation.ChartPage'
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        chart_page = value['chart_page']
        context['chart'] = chart_page.specific if chart_page and chart_page.live else ''
        return context


class AdvancedInteractiveChartBlock(StructBlock):

    class Meta:
        help_text = 'Select an advanced chart page'
        icon = 'fa-area-chart'
        label = 'Advanced Interactive Chart'
        template = 'publications/blocks/interactive_chart.html'
        form_template = 'publications/block_forms/custom_struct.html'

    show_title = BooleanBlock(required=False, default=True)
    allow_share = BooleanBlock(required=False, default=True)
    chart_page = PageChooserBlock(
        page_type=['visualisation.AdvancedChartPage','visualisation.RawCodePage']
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        chart_page = value['chart_page']
        context['chart'] = chart_page.specific if chart_page and chart_page.live else ''
        return context


def flexible_content_streamfield(blank=False):
    return StreamField([
        ('captioned_image', CaptionedImage()),
        ('case_study', CaseStudy()),
        ('definition_list', DefinitionList()),
        ('block_quote', SectionBlockQuote(template='blocks/publication_blockquote.html')),
        ('downloads', Downloads()),
        ('section_heading', SectionHeading()),
        ('table', Table()),
        ('pivot_table', PivotTable()),
        ('dynamic_table', DynamicTable()),
        ('rich_text', RichText()),
        ('infographic', PublicationInfographic()),
        ('anchor', AnchorBlock()),
        ('interactive_chart', InteractiveChartBlock()),
        ('advanced_interactive_chart', AdvancedInteractiveChartBlock()),
        ('cta', CallToActionBlock()),
        ('accordion', AccordionBlock())

    ], blank=blank, use_json_field=True)


def content_streamfield(blank=False):
    return StreamField([
        ('captioned_image', CaptionedImage()),
        ('definition_list', DefinitionList()),
        ('table', Table()),
        ('rich_text', RichTextNoFootnotes()),
        ('anchor', AnchorBlock()),
    ], blank=blank, use_json_field=True)
