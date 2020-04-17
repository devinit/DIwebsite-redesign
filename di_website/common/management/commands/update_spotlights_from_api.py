import requests
from json.decoder import JSONDecodeError

from django.core.management.base import BaseCommand

from di_website.spotlight.models import SpotlightIndicator, SpotlightPage, SpotlightTheme
from di_website.spotlight.snippets import SpotlightColour


class Command(BaseCommand):
    """
    Downloads Spotlight data from the GitHub CMS
    """
    base_url = 'https://raw.githubusercontent.com/'

    def add_arguments(self, parser):
        """Add custom command arguments."""
        parser.add_argument('base_url', nargs='?', type=str, default='http://178.128.102.213/')


    def handle(self, *args, **options):
        endpoint = options['base_url'] + 'api/spotlights/pages/'

        try:
            pages = self.fetch_data(endpoint)

            for page in pages:
                self.handle_page(page)
        except JSONDecodeError:
            print('Something went wrong while fetching data. Please make sure the endpoint is reachable')


    def fetch_data(self, endpoint):
        # Fetch Spotlights
        response = requests.get(endpoint)

        return response.json()


    def handle_page(self, page):
        slug = self.get_slug_from_relative_url(page['relative_url'])
        spotlight_page = self.get_spotlight_page_from_slug(slug)

        if not spotlight_page:
            spotlight_page = self.create_spotlight_page(page)

        themes = page['themes']
        for theme in themes:
            self.handle_theme(spotlight_page, theme)


    def handle_theme(self, spotlight, theme):
        spotlight_theme = self.get_spotlight_theme_from_slug(spotlight, theme['slug'])

        if not spotlight_theme:
            spotlight_theme = self.create_spotlight_theme(spotlight, theme)

        for indicator in theme['indicators']:
            self.handle_indicator(spotlight_theme, indicator)


    def handle_indicator(self, theme, indicator):
        spotlight_indicator = self.get_spotlight_indicator_from_slug(theme, indicator['slug'])

        if not spotlight_indicator:
            spotlight_indicator = self.create_spotlight_indicator(theme, indicator)

        self.update_spotlight_indicator(spotlight_indicator, indicator)


    def get_slug_from_relative_url(self, relative_url):
        bits = relative_url.split('/')

        return bits[len(bits) - 2]


    def get_spotlight_page_from_slug(self, slug):
        try:
            spotlight_page = SpotlightPage.objects.filter(slug=slug)[0]

            return spotlight_page
        except IndexError:
            return None


    def create_spotlight_page(self, page):
        slug = self.get_slug_from_relative_url(page['relative_url'])
        spotlight = SpotlightPage(
            title=page['title'],
            slug=slug,
            country_code=page['country_code'],
            country_name=page['country_name'],
            currency_code=page['currency_code'],
            datasources_description=page['datasources_description'])

        return spotlight


    def get_spotlight_theme_from_slug(self, spotlight, slug):
        try:
            matching_page = spotlight.get_children().filter(slug=slug)[0]

            return matching_page
        except IndexError:
            return None


    def create_spotlight_theme(self, spotlight, theme):
        theme = SpotlightTheme(title=theme['name'], slug=theme['slug'], section=theme['section'])
        spotlight.add_child(instance=theme)
        theme.save_revision().publish()
        spotlight.save()

        return theme


    def get_spotlight_indicator_from_slug(self, theme, slug):
        try:
            matching_page = theme.get_children().filter(slug=slug)[0]

            return matching_page
        except IndexError:
            return None


    def create_spotlight_indicator(self, theme, indicator):
        colour = self.get_colour_by_code(indicator['colour'])
        indicator = SpotlightIndicator(
            title=indicator['name'],
            slug=indicator['slug'],
            ddw_id=indicator['ddw_id'],
            description=indicator['description'],
            start_year=indicator['start_year'] or None,
            end_year=indicator['end_year'] or None,
            excluded_years=indicator['excluded_years'] or '',
            data_format=indicator['data_format'],
            range=indicator['range'] or '',
            value_prefix=indicator['value_prefix'],
            value_suffix=indicator['value_suffix'],
            tooltip_template=indicator['tooltip_template'],
            content_template=indicator['content_template'],
            source=indicator['source'],
            color=colour)
        theme.add_child(instance=indicator)
        indicator.save_revision().publish()
        theme.save()

        return theme


    def update_spotlight_indicator(self, spotlight_indicator, indicator):
        colour = self.get_colour_by_code(indicator['colour'])
        spotlight_indicator.title = indicator['name']
        spotlight_indicator.slug = spotlight_indicator.slug or indicator['slug']
        spotlight_indicator.ddw_id = spotlight_indicator.ddw_id if hasattr(spotlight_indicator, 'ddw_id') else indicator['ddw_id']
        spotlight_indicator.description = indicator['description']
        spotlight_indicator.start_year = indicator['start_year'] or None
        spotlight_indicator.end_year = indicator['end_year'] or None
        spotlight_indicator.excluded_years = indicator['excluded_years'] or ''
        spotlight_indicator.data_format = indicator['data_format']
        spotlight_indicator.range = indicator['range'] or ''
        spotlight_indicator.value_prefix = indicator['value_prefix']
        spotlight_indicator.value_suffix = indicator['value_suffix']
        spotlight_indicator.tooltip_template = indicator['tooltip_template']
        spotlight_indicator.content_template = indicator['content_template']
        spotlight_indicator.source = indicator['source']
        spotlight_indicator.colour = colour

        spotlight_indicator.save()


    def get_colour_by_code(self, code):
        try:
            colour = SpotlightColour.objects.filter(code=code)[0]

            return colour
        except IndexError:
            return None
