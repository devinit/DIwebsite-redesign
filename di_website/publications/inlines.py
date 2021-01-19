from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import PageChooserPanel

from di_website.downloads.models import DownloadItem, DataDownloadItem


class PublicationPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationPage', related_name='publication_downloads')


class PublicationPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationPage', related_name='data_downloads')


class PublicationSummaryPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationSummaryPage', related_name='publication_downloads')


class PublicationForewordPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('PublicationForewordPage', related_name='publication_downloads')


class PublicationSummaryPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationSummaryPage', related_name='data_downloads')


class PublicationForewordPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('PublicationForewordPage', related_name='data_downloads')


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


class ShortPublicationPageDownloads(Orderable, DownloadItem):
    item = ParentalKey('ShortPublicationPage', related_name='publication_downloads')


class ShortPublicationPageDataDownloads(Orderable, DataDownloadItem):
    item = ParentalKey('ShortPublicationPage', related_name='data_downloads')


class PublicationDataset(Orderable):
    class Meta(Orderable.Meta):
        abstract = True

    dataset = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [PageChooserPanel('dataset', ['datasection.DatasetPage'])]


class PublicationPageDataset(PublicationDataset):
    item = ParentalKey('PublicationPage', related_name='publication_datasets')


class PublicationSummaryPageDataset(PublicationDataset):
    item = ParentalKey('PublicationSummaryPage', related_name='publication_datasets')


class PublicationForewordPageDataset(PublicationDataset):
    item = ParentalKey('PublicationForewordPage', related_name='publication_datasets')


class PublicationChapterPageDataset(PublicationDataset):
    item = ParentalKey('PublicationChapterPage', related_name='publication_datasets')


class PublicationAppendixPageDataset(PublicationDataset):
    item = ParentalKey('PublicationAppendixPage', related_name='publication_datasets')


class LegacyPublicationPageDataset(PublicationDataset):
    item = ParentalKey('LegacyPublicationPage', related_name='publication_datasets')


class ShortPublicationPageDataset(PublicationDataset):
    item = ParentalKey('ShortPublicationPage', related_name='publication_datasets')
