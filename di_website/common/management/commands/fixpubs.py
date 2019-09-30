"""Management command that fixes imported WP content."""

import json
import os
import re

from django.conf import settings
from django.core.management.base import BaseCommand

from di_website.publications.models import LegacyPublicationPage


class Command(BaseCommand):
    """Management command that imports news from a JSON file."""

    help = 'Fix publications given a JSON file.'

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('pubs_file', nargs='?', type=str, default=os.path.join(settings.BASE_DIR, 'migrated_content/di_pubs.json'))

    def handle(self, *args, **options):
        """Implement the command handler."""

        with open(options['pubs_file']) as pubs_file:
            publication_datasets = json.load(pubs_file)
            for publication_dataset in publication_datasets:

                slug = publication_dataset['url'].split('/')[-2]
                pub_check = LegacyPublicationPage.objects.filter(slug=slug)
                if pub_check:
                    pub_page = pub_check.first()
                    clean_body = re.sub(r'Modal[\s\S]*\/Modal', '', publication_dataset['body'])
                    clean_body = re.sub('btn btn--dark pdf-download', 'button', clean_body)
                    pub_page.raw_content = clean_body
                    pub_page.content = ""
                    pub_page.save_revision().publish()

        self.stdout.write(self.style.SUCCESS('Successfully fixed publications.'))
