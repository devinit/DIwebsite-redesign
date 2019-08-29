from wagtail.admin.edit_handlers import StreamFieldPanel
from .edit_handlers import MultiFieldPanel
from collections import defaultdict


def get_downloads(instance, with_parent=False, data=False):
    d = defaultdict(list)
    downloads = instance.data_downloads.all() if data else instance.downloads.all()

    for item in downloads:
        download = create_download(item)
        d[download[0]].append(download[1])

    if with_parent:
        if data:
            parent_downloads = instance.get_parent().specific.data_downloads.all()
        else:
            parent_downloads = instance.get_parent().specific.downloads.all()

        for item in parent_downloads:
            download = create_download(item)
            d[download[0]].append(download[1])

    return d.items()


def create_download(item):
    download = {
        'prefix': '',
        'download': item.download
    }

    try:
        language = item.download.language.title
    except AttributeError:
        language = ''

    return (language, download, )


def ContentPanel(heading='Content', description='Main content for the page. Build page content by adding new rows from the available content types.'):
    return MultiFieldPanel(
        [
            StreamFieldPanel('content'),
        ],
        heading=heading,
        description=description,
    )
