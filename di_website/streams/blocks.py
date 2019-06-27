
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)

class StaffProfileBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    name = CharBlock(required=True,max_length=150)
    position = CharBlock(required=True,max_length=300)

    class Meta:
        icon="placeholder"
        template="streams/staff_profile.html"