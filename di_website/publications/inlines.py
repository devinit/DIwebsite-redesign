from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable

from di_website.downloads.models import (
    DownloadItem, DataDownloadItem, DownloadGroupItem, DownloadImageGroupItem)


class PublicationPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationPage', related_name='publication_downloads')


class PublicationPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationPage', related_name='data_downloads')


class PublicationSummaryPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationSummaryPage', related_name='publication_downloads')


class PublicationSummaryPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationSummaryPage', related_name='data_downloads')


class PublicationChapterPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationChapterPage', related_name='publication_downloads')


class PublicationChapterPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationChapterPage', related_name='data_downloads')

class PublicationAppendixPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationAppendixPage', related_name='publication_downloads')


class PublicationAppendixPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationAppendixPage', related_name='data_downloads')


class LegacyPublicationPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('LegacyPublicationPage', related_name='publication_downloads')


class LegacyPublicationPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('LegacyPublicationPage', related_name='data_downloads')


class LegacyPublicationPageDownloadGroups(Orderable, DownloadGroupItem):
    item = ParentalKey('LegacyPublicationPage', related_name='download_groups')
