from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock
)
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class TeamMemberQuoteBlock(StructBlock):
    quote_text = TextBlock()
    team_member = PageChooserBlock(page_type='ourteam.TeamMemberPage', required=False)

    class Meta():
        icon = 'fa-users'


class ExternalMemberQuoteBlock(StructBlock):
    quote_text = TextBlock()
    name = TextBlock()
    role = TextBlock()
    organisation = TextBlock()
    external_member_photo = ImageChooserBlock(required=False)

    class Meta():
        icon = 'fa-user'


class QuoteStreamBlock(StreamBlock):
    team_member = TeamMemberQuoteBlock()
    external_member = ExternalMemberQuoteBlock()
    required = False


class MetaDataDescriptionBlock(StructBlock):
    description = RichTextBlock(icon="title", required=False)
    provenance = RichTextBlock(icon="title", required=False)
    variables = RichTextBlock(icon="title", required=False)
    geography = RichTextBlock(icon="title", required=False)
    topic = RichTextBlock(icon="title", required=False)


class MetaDataSourcesBlock(StructBlock):
    data_sources = PageChooserBlock(page_type="datasection.DatasetPage", required=False)


class MetaDataSourcesStreamBlock(StreamBlock):
    description = RichTextBlock(icon="title", required=False)
    sources = MetaDataSourcesBlock()
