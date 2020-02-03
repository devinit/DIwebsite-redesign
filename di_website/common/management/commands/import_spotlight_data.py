import pandas
import math

from django.core.management.base import BaseCommand

from di_website.spotlight.snippets import (
    SpotlightColour, Spotlight, SpotlightIndicator, SpotlightSource, SpotlightTheme)


class Command(BaseCommand):
    """
    Imports Spotlight data from the files downloaded from the GitHub CMS into Wagtail
    """

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('branch', nargs='?', type=str, default='master')

    def handle(self, *args, **options):
        self.import_colours()
        self.import_uganda_themes()
        self.import_uganda_indicators()

    def import_colours(self):
        SpotlightColour.objects.all().delete()

        try:
            file_name = 'spotlight-colors.csv'
            data = pandas.read_csv(file_name)
            for _, j in data.iterrows():
                colour = SpotlightColour(name=j['id'], code=j['value'])
                colour.save()
        except FileNotFoundError:
            print('No import of colour data done. File "spotlight-colors.csv" not found')

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
            print('No import of Uganda theme data done. File "spotlight-uganda-theme.csv" not found')

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

    def import_uganda_indicators(self):
        SpotlightIndicator.objects.all().delete()
        try:
            file_name = 'spotlight-uganda-concept.csv'
            data = pandas.read_csv(file_name)
            spotlight = self.get_spotlight_by_slug('spotlight-uganda')
            if not spotlight:
                print('Please first create a Spotlight snippet and import the related themes')

                return

            for _, j in data.iterrows():
                theme = self.get_theme_by_slug_and_spotlight(j['theme'], spotlight)
                if not theme:
                    continue
                colour = self.get_colour_by_name(j['color'])
                source = self.get_source_by_name(j['source'])
                start_year = None if math.isnan(j['start_year']) else j['start_year']
                end_year = None if math.isnan(j['end_year']) else j['end_year']

                indicator = SpotlightIndicator(
                    ddw_id=j['id'], name=j['name'], description=j['description'],
                    theme=theme, color=colour, source=source, start_year=start_year,
                    end_year=end_year, range=j['range'], value_prefix=j['uom_display'],
                    tooltip_template=j['tooltip'])
                indicator.save()
            print('Uganda indicators successfully imported')
        except FileNotFoundError:
            print('No import of Uganda theme data done. File "spotlight-uganda-theme.csv" not found')

    def get_spotlight_by_slug(self, slug, name=None):
        try:
            spotlight = Spotlight.objects.filter(slug=slug)[0]

            return spotlight
        except IndexError:
            if name:
                spotlight = Spotlight(name=name, slug=slug)

                return spotlight

            return None

    def get_theme_by_slug_and_spotlight(self, slug, spotlight):
        try:
            theme = SpotlightTheme.objects.filter(slug=slug, spotlight=spotlight)[0]

            return theme
        except IndexError:
            return None

    def get_colour_by_name(self, name):
        try:
            colour = SpotlightColour.objects.filter(name=name)[0]

            return colour
        except IndexError:
            return None

    def get_source_by_name(self, name):
        try:
            source = SpotlightSource.objects.filter(name=name)[0]

            return source
        except IndexError:
            source = SpotlightSource(name=name)
            source.save()

            return source
