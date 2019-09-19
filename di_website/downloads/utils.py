from wagtail.admin.edit_handlers import InlinePanel
from di_website.publications.edit_handlers import MultiFieldPanel


def DownloadsPanel(related_name='publication_downloads', label='Download', heading='Downloads', description='Optional: add one or more downloads to the page.', max_num=None):
    return MultiFieldPanel(
        [
            InlinePanel(related_name, label=label, max_num=max_num),
        ],
        heading=heading,
        description=description
    )


def DownloadGroupsPanel(related_name='download_groups', label='Download group', heading='Download groups', description='Optional: add one or more download groups to the page.', max_num=None):
    return MultiFieldPanel(
        [
            InlinePanel(related_name, label=label, max_num=max_num),
        ],
        heading=heading,
        description=description
    )
