from wagtail.blocks import (
    CharBlock,
    DateBlock,
    ListBlock,
    StructBlock,
    TextBlock
)
from wagtail.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


download_streamfield = StreamField([
    ('items', ListBlock(
        StructBlock(
            [
                ('title', CharBlock()),
                ('description', TextBlock(required=False)),
                ('file', DocumentChooserBlock()),
            ],
            template='downloads/blocks/item.html',
            form_classname='custom__itemlist struct-block'
        ),
        template='content/blocks/list.html',
        label='Add download'
    ))
], use_json_field=True)

download_image_streamfield = StreamField([
    ('items', ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', CharBlock()),
                ('description', TextBlock(required=False)),
                ('file', DocumentChooserBlock()),
            ],
            template='downloads/blocks/item_image.html',
            form_classname='custom__itemlist struct-block'
        ),
        template='content/blocks/list.html',
        label='Add download'
    ))
], use_json_field=True)

download_date_streamfield = StreamField([
    ('items', ListBlock(
        StructBlock(
            [
                ('date', DateBlock()),
                ('title', CharBlock()),
                ('description', TextBlock(required=False)),
                ('file', DocumentChooserBlock()),
            ],
            template='downloads/blocks/item_date.html',
            form_classname='custom__itemlist struct-block'
        ),
        template='content/blocks/list.html',
        label='Add download'
    ))
], use_json_field=True)
