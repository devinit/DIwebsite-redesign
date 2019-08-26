from wagtail.admin.edit_handlers import StreamFieldPanel
from .edit_handlers import MultiFieldPanel


def ContentPanel(heading='Content', description='Main content for the page. Build page content by adding new rows from the available content types.'):
    return MultiFieldPanel(
        [
            StreamFieldPanel('content'),
        ],
        heading=heading,
        description=description,
    )
