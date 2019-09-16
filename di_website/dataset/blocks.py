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


class MainContentBlock(StreamBlock):
    """
    Renders a map with all the DI office locations
    """
    release_date = DateBlock()
    text_content = RichTextBlock(required=False)
    most_recent_dataset = PageChooserBlock(page_type="dataset.DatasetPage", required=False)

    class Meta():
        icon = 'fa-edit'
        template = 'blocks/dataset_main_content.html'
