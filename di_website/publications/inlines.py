from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

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


class PublicationCallToAction(Orderable):
    item = ParentalKey('PublicationPage', related_name='publication_cta')
    CTA_POSITION_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('top-bottom', 'Top & Bottom'),
    ]

    title = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="Optional: when left blank, the call to action will not be show",
        verbose_name='Title'
    )
    body = models.TextField(
        null=True, blank=True, verbose_name='Description',
        help_text='Optional: describe the purpose of your call to action in a bit more detail')
    button_text = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Button Caption',
        help_text='Optional: this is required to show the button')
    button_url = models.URLField(
        max_length=255, null=True, blank=True, verbose_name='Button URL',
        help_text='Optional: this is required to show the button')
    position = models.CharField(
        max_length=100, null=True, blank=True, choices=CTA_POSITION_CHOICES, verbose_name='Position', default='top')
    inherit = models.BooleanField(default=True, help_text='Optional: show this CTA on child pages')

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        FieldPanel('button_text'),
        FieldPanel('button_url'),
        FieldPanel('inherit'),
        FieldPanel('position'),
    ]
