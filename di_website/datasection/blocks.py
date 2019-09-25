from django.db import models

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

from di_website.common.constants import RICHTEXT_FEATURES
from di_website.common.blocks import LinkBlock


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
    description = TextBlock()
    telephone = TextBlock()
    email = EmailBlock()
    photo = ImageChooserBlock(required=False)
    photographer = TextBlock()
    photo_credit = URLBlock()

    class Meta():
        icon = 'fa-phone-square'


class DataSuportStreamBlock(StreamBlock):
    support = DataSupportServicesBlock()
    required = False

    class Meta():
        max_num=1
