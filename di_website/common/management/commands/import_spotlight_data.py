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
        # Find Spotlight on Uganda Page
        try:
            uganda = Spotlight.objects.filter(slug='spotlight-uganda')[0]
        except IndexError:
            uganda = Spotlight(name='Spotlight on Uganda', slug='spotlight-uganda')

        SpotlightTheme.objects.filter(spotlight=uganda).delete()
        # Theme Indicators
        try:
            theme_file_name = 'uganda-theme.csv'
            data = pandas.read_csv(theme_file_name)
            for _, j in data.iterrows():
                theme = SpotlightTheme(name=j['name'], spotlight=uganda)
                theme.save()
            print('Uganda theme data successfully imported')
        except FileNotFoundError: # FIXME: proper error handling
            print('No import of Uganda theme data done. File "theme.csv" not found')

        # os.remove(indicator_file_name)
