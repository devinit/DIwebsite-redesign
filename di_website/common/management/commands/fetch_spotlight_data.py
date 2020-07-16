import requests

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Downloads Spotlight data from the GitHub CMS
    """
    base_url = 'https://raw.githubusercontent.com/'

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('branch', nargs='?', type=str, default='master')

    def handle(self, *args, **options):
        content_path = 'devinit/datahub-cms/' + options['branch']

        self.fetch_colours(content_path)

        self.fetch_data(content_path + '/spotlight-uganda/', prefix='spotlight-uganda-')
        self.fetch_data(content_path + '/spotlight-kenya/', prefix='spotlight-kenya-')

    def fetch_colours(self, content_path):
        content_url = self.base_url + content_path + '/global/'
        file_name = 'colors.csv'
        self.fetch_csv(file_name, content_url, 'spotlight-')

    def fetch_data(self, content_path, prefix):
        content_url = self.base_url + content_path
        # Fetch Indicators
        indicator_file_name = 'concept.csv'
        self.fetch_csv(indicator_file_name, content_url, prefix)

        # Fetch Themes
        theme_file_name = 'theme.csv'
        self.fetch_csv(theme_file_name, content_url, prefix)

    def fetch_csv(self, file_name, url, csv_prefix):
        """Fetch CSV data from GitHub content URL

        Arguments:
            file_name {string} -- Name of the file in the GitHub folder
            url {string} -- Base GitHub URL
            csv_prefix {string} -- Used to ensure unique filenames when saving
        """
        response = requests.get(url + file_name)
        csv_file = open(csv_prefix + file_name, 'w')
        csv_file.write(response.text)
