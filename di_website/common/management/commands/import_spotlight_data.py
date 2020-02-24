import csv

from django.core.management.base import BaseCommand

from di_website.spotlight.models import SpotlightPage, SpotlightIndicator, SpotlightTheme
from di_website.spotlight.snippets import SpotlightColour, SpotlightSource
from di_website.datasection.models import DataSectionPage


class Command(BaseCommand):
    """
    Imports Spotlight data from the files downloaded from the GitHub CMS into Wagtail
    """

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('branch', nargs='?', type=str, default='master')

    def handle(self, *args, **options):
        self.import_colours()
        SpotlightPage.objects.all().delete()
        self.import_uganda_themes()
        self.import_indicators('spotlight-uganda', 'uganda_')
        self.import_kenya_themes()
        self.import_indicators('spotlight-kenya', 'kenya_')

    def import_colours(self):
        SpotlightColour.objects.all().delete()

        try:
            file_name = 'spotlight-colors.csv'
            with open(file_name, 'rt') as my_file:
                reader = csv.reader(my_file)
                count = 0
                for row in reader:
                    if count != 0:
                        colour = SpotlightColour(name=row[0], code=row[1])
                        colour.save()
                    count += 1
        except FileNotFoundError:
            print('No import of colour data done. File "spotlight-colors.csv" not found')

    def import_uganda_themes(self):
        """Import uganda themes from the csv file
        """
        # Find Spotlight on Uganda Page
        try:
            uganda = SpotlightPage.objects.filter(slug='spotlight-uganda')[0]
        except IndexError:
            data_page = DataSectionPage.objects.live()[0]
            if (data_page):
                uganda = SpotlightPage(
                    title='Spotlight on Uganda',
                    slug='spotlight-uganda',
                    country_code='UG',
                    currency_code='UGX')
                data_page.add_child(instance=uganda)
                uganda.save_revision().publish()
                data_page.save();
            else:
                print('Cannot create SpotlightPage ... No DataSection page found')

        # Spotlight Themes
        try:
            theme_file_name = 'spotlight-uganda-theme.csv'
            self.create_themes_from_csv(theme_file_name, uganda, "uganda_")
            print('Uganda theme data successfully imported')
        except FileNotFoundError:
            print('No import of Uganda theme data done. File "spotlight-uganda-theme.csv" not found')

    def import_kenya_themes(self):
        """Import Kenya themes from the csv file
        """
        # Find Spotlight on Uganda Page
        try:
            spotlight = SpotlightPage.objects.filter(slug='spotlight-kenya')[0]
        except IndexError:
            data_page = DataSectionPage.objects.live()[0]
            if (data_page):
                spotlight = SpotlightPage(
                    title='Spotlight on Kenya',
                    slug='spotlight-kenya',
                    country_code='KE',
                    currency_code='KES')
                data_page.add_child(instance=spotlight)
                spotlight.save_revision().publish()
                data_page.save();
            else:
                print('Cannot create SpotlightPage ... No DataSection page found')

        # Spotlight Themes
        try:
            theme_file_name = 'spotlight-kenya-theme.csv'
            self.create_themes_from_csv(theme_file_name, spotlight, "kenya_")
            print('Kenya theme data successfully imported')
        except FileNotFoundError:
            print('No import of Kenya theme data done. File "spotlight-kenya-theme.csv" not found')

    def create_themes_from_csv(self, file_name, spotlight, prefix):
        """Create theme objects from processed csv file

        Arguments:
            file_name {string} -- The name of the csv file that contains the theme data
            spotlight {Spotlight} -- The Spotlight model object to relate to the theme
        """
        with open(file_name, 'rt') as my_file:
            reader = csv.reader(my_file)
            count = 0
            for row in reader:
                if count != 0:
                    theme = SpotlightTheme(slug=prefix + row[0], title=row[1])
                    spotlight.add_child(instance=theme)
                    theme.save_revision().publish()
                    theme.save()
                count += 1

    def import_indicators(self, slug, prefix):
        try:
            file_name = slug + '-concept.csv'
            spotlight = self.get_spotlight_by_slug(slug)
            if not spotlight:
                print('Please first create a Spotlight snippet and import the related themes')

                return

            with open(file_name, 'rt') as my_file:
                reader = csv.reader(my_file)
                count = 0
                for row in reader:
                    if count != 0:
                        theme = self.get_theme_by_slug_and_spotlight(prefix + row[1], spotlight)
                        if not theme:
                            print('No theme found with slug ' + row[1] + ' for spotlight slug ' + spotlight.slug)
                            continue
                        colour = self.get_colour_by_name(row[2])
                        source = self.get_source_by_name(row[14])
                        try:
                            start_year = int(row[3])
                        except ValueError:
                            start_year = None

                        try:
                            end_year = int(row[4])
                        except ValueError:
                            end_year = None

                        indicator = SpotlightIndicator(
                            ddw_id=row[0], title=row[10], description=row[13], color=colour, source=source,
                            start_year=start_year, end_year=end_year, range=row[5], value_suffix=row[7],
                            tooltip_template=row[12])
                        theme.add_child(instance=indicator)
                        indicator.save_revision().publish()
                        theme.save()
                    count += 1
            print(slug + ' indicators successfully imported')
        except FileNotFoundError:
            print('No import of ' + slug + ' theme data done. File "' + slug + '-theme.csv" not found')

    def get_spotlight_by_slug(self, slug, name=None):
        try:
            spotlight = SpotlightPage.objects.filter(slug=slug)[0]

            return spotlight
        except IndexError:
            if name:
                spotlight = SpotlightPage(title=name, slug=slug)

                return spotlight

            return None

    def get_theme_by_slug_and_spotlight(self, slug, spotlight):
        try:
            theme = spotlight.get_children().filter(slug=slug)[0]

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
