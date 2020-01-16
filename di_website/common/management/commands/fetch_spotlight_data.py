import requests

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Downloads Spotlight data from the GitHub CMS
    """

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('branch', nargs='?', type=str, default='master')

    def handle(self, *args, **options):
        base_url = 'https://raw.githubusercontent.com/'
        content_path = 'devinit/datahub-cms/' + options['branch']

        # Fetch Indicators
        indicator_file_name = 'concept.csv'
        response = requests.get(base_url + content_path + '/spotlight-uganda/' + indicator_file_name)
        indicator_file = open('uganda-' + indicator_file_name, 'w')
        indicator_file.write(response.text)

        # Fetch Themes
        theme_file_name = 'theme.csv'
        response = requests.get(base_url + content_path + '/spotlight-uganda/' + theme_file_name)
        theme_file = open('uganda-' + theme_file_name, 'w')
        theme_file.write(response.text)
