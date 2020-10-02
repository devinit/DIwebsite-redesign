"""Management command that erases datasets."""


from django.core.management.base import BaseCommand

from di_website.publications.inlines import (
    PublicationPageDataset, PublicationSummaryPageDataset,
    PublicationChapterPageDataset, PublicationAppendixPageDataset,
    LegacyPublicationPageDataset, ShortPublicationPageDataset
)

from di_website.datasection.models import DataSource, DatasetPage


class Command(BaseCommand):
    """Management command erases datasection content"""

    help = 'Erase metadata'

    def handle(self, *args, **options):

        DataSource.objects.all().delete()
        DatasetPage.objects.all().delete()
        PublicationPageDataset.objects.all().delete()
        PublicationSummaryPageDataset.objects.all().delete()
        PublicationChapterPageDataset.objects.all().delete()
        PublicationAppendixPageDataset.objects.all().delete()
        LegacyPublicationPageDataset.objects.all().delete()
        ShortPublicationPageDataset.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Called successfully'))
