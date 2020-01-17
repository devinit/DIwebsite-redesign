import pandas

from django.core.management.base import BaseCommand

from di_website.spotlight.snippets import Spotlight, SpotlightTheme


class Command(BaseCommand):
    """
    Imports Spotlight data from the files downloaded from the GitHub CMS into Wagtail
    """

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('branch', nargs='?', type=str, default='master')

    def handle(self, *args, **options):
        self.import_uganda_themes()

    def import_uganda_themes(self):
        """Import uganda themes from the csv file
        """
        # Find Spotlight on Uganda Page
        try:
            uganda = Spotlight.objects.filter(slug='spotlight-uganda')[0]
        except IndexError:
            uganda = Spotlight(name='Spotlight on Uganda', slug='spotlight-uganda')

        SpotlightTheme.objects.filter(spotlight=uganda).delete()
        # Spotlight Themes
        try:
            theme_file_name = 'spotlight-uganda-theme.csv'
            self.create_themes_from_csv(theme_file_name, uganda)
            print('Uganda theme data successfully imported')
        except FileNotFoundError:
            print('No import of Uganda theme data done. File "theme.csv" not found')

    def create_themes_from_csv(self, file_name, spotlight):
        """Create theme objects from processed csv file

        Arguments:
            file_name {string} -- The name of the csv file that contains the theme data
            spotlight {Spotlight} -- The Spotlight model object to relate to the theme
        """
        data = pandas.read_csv(file_name)
        for _, j in data.iterrows():
            theme = SpotlightTheme(name=j['name'], slug=j['id'], spotlight=spotlight)
            theme.save()
