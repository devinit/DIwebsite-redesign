from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
    EmailBlock
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


class DataSupportServicesBlock(StructBlock):
    title = TextBlock()
    description = TextBlock(required=False)
    telephone = TextBlock(required=False)
    email = EmailBlock(required=False)
    photo = ImageChooserBlock(required=False)
    photographer = TextBlock(required=False)
    photo_credit = URLBlock(required=False)

    class Meta():
        icon = 'fa-phone-square'


class DataSuportStreamBlock(StreamBlock):
    support = DataSupportServicesBlock()
    required = False
