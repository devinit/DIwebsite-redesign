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
    URLBlock,
    DateBlock
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.blocks import ButtonBlock


class MetaDataDescriptionBlock(StructBlock):
    description = RichTextBlock(icon="title", required=False)
    provenance = RichTextBlock(icon="title", required=False)
    variables = RichTextBlock(icon="title", required=False)
    geography = RichTextBlock(icon="title", required=False)
    topic = RichTextBlock(icon="title", required=False)


class MetaDataSourcesBlock(StructBlock):
    data_sources = PageChooserBlock(page_type="dataset.DatasetPage", required=False)


class MetaDataSourcesStreamBlock(StreamBlock):
    description = RichTextBlock(icon="title", required=False)
    sources = MetaDataSourcesBlock()
