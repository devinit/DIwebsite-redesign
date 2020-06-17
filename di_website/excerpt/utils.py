from wagtail.admin.edit_handlers import FieldPanel
from di_website.publications.edit_handlers import MultiFieldPanel


def ExcerptPanel():
    return MultiFieldPanel(
        [
            FieldPanel('excerpt_field'),
        ],
        heading='Excerpt',
        description='Optional: handcrafted excerpt to be displayed in listings.'
    )
