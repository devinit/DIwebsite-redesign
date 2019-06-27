
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core.blocks import (
    CharBlock, 
    ChoiceBlock,
    RichTextBlock, 
    StreamBlock, 
    StructBlock, 
    TextBlock,
    ListBlock,
    BooleanBlock,
    PageChooserBlock
)
from di_website.ourteam import constants

class TeamProfileBlock(StructBlock):

    """ Team profile displayed on our team page """
    profiles = ListBlock(
        StructBlock(
            [
                ("image",ImageChooserBlock(required=False)),
                ("name", CharBlock(required=True,max_length=150)),
                ("position",CharBlock(required=True,max_length=300)),
                ("department",ChoiceBlock(choices=constants.DEPARTMENTS, icon='tag')),
                ("page_link",PageChooserBlock(required=False)),
                ("active",BooleanBlock(required=True,help_text=" Uncheck if team member no longer with DI")),
            ]
        )
    )

    class Meta:
        icon="placeholder"
        template="streams/staff_profile.html"
        label="Our Team"