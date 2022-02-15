"""Management command that replaces old hashbang links."""

import json
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from di_website.publications.models import LegacyPublicationPage, PublicationType


class Command(BaseCommand):
    """Management command that fixed aidtransparency links."""

    help = 'Replace links given a JSON file.'

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('json_file', nargs='+', type=str)

    def handle(self, *args, **options):
        """Implement the command handler."""
        discussion_paper = PublicationType.objects.get(name="Discussion paper")

        with open(options['json_file'][0]) as json_file:
            json_data = json.load(json_file)

        all_pages = LegacyPublicationPage.objects.live()

        for page in all_pages:
            for replacement in json_data:
                old_link = '"' + replacement["OldLink"] + '"'
                new_link = '"' + replacement["NewLink"] + '"'
                old_content = page.raw_content
                if old_link in old_content:
                    self.stdout.write(self.style.SUCCESS("Replacing old link in page: " + page.slug))
                    new_content = old_content.replace(old_link, new_link)
                    page.raw_content = new_content
                    try:
                        page.save()
                    except ValidationError:
                        page.publication_type = discussion_paper
                        page.save()

        self.stdout.write(self.style.SUCCESS("Done."))