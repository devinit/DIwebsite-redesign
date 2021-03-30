import csv
import json
import shutil
import tempfile
import urllib.request

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from github import Github
from wagtail.core.models import Site

from di_website.datasection.models import DataSectionPage
from di_website.home.templatetags.footer_tags import get_footer_text
from di_website.home.templatetags.navigation_tags import get_menu_items
from di_website.spotlight.models import (SpotlightLocationComparisonPage,
                                         SpotlightPage, SpotlightTheme)

from .utils import (fetch_and_serialise_footer_sections,
                    fetch_and_serialise_newsletters,
                    serialise_location_comparison_page, serialise_page,
                    serialise_spotlight_theme, serialiseDatasources)


@require_http_methods(["GET"])
def spotlights_navigation_view(request):
    """
    Handles the /api/spotlights/navigation/ endpoint, returning the navigation links (pri & seco)
    """
    navigation = {'primary': [], 'secondary': []}
    root_page = Site.find_for_request(request).root_page
    data_section_page = DataSectionPage.objects.live().first()
    primary_menu_items = get_menu_items(root_page, data_section_page)
    for menu_item in primary_menu_items:
        navigation['primary'].append(serialise_page(request, menu_item))
    if data_section_page:
        secondary_menu_items = get_menu_items(data_section_page, None) # FIXME: replace calling page with SpotlightsPage
        for menu_item in secondary_menu_items:
            navigation['secondary'].append(serialise_page(request, menu_item))

    return JsonResponse(navigation, safe=False)


@require_http_methods(["GET"])
def footer_view(request):
    """
    Handles the /api/footer endpoint, returning content required to render the footer
    """
    footer_text = get_footer_text()
    footer = {
        'newsletters': fetch_and_serialise_newsletters(),
        'footer_text': footer_text['footer_text'],
        'footer_text_major': footer_text['footer_text_major'],
        'sections': fetch_and_serialise_footer_sections(request)
    }

    return JsonResponse(footer, safe=False)


@require_http_methods(["GET"])
def spotlight_pages_view(request):
    pages = []
    spotlights = SpotlightPage.objects.all().live()
    for spotlight in spotlights:
        page = serialise_page(request, spotlight, fields=['title', 'full_url', 'country_code', 'country_name', 'currency_code', 'datasources_description'])
        themes = spotlight.get_children().live().type(SpotlightTheme)
        location_comparison_pages = spotlight.get_children().live().type(SpotlightLocationComparisonPage)
        page['compare'] = serialise_location_comparison_page(location_comparison_pages)
        page['themes'] = []
        for theme in themes:
            serialised_theme = serialise_spotlight_theme(theme.specific)
            page['themes'].append(serialised_theme)
        pages.append(page)

    return JsonResponse(pages, safe=False)


@require_http_methods(["GET"])
def spotlight_page_view(request, slug=None):
    if slug:
        try:
            spotlight = SpotlightPage.objects.filter(slug=slug)[0]
            page = serialise_page(request, spotlight, fields=['title', 'full_url', 'country_code', 'country_name', 'currency_code', 'datasources_description'])
            page['datasource_links'] = serialiseDatasources(request, spotlight)
            themes = spotlight.get_children().live().type(SpotlightTheme)
            location_comparison_pages = spotlight.get_children().live().type(SpotlightLocationComparisonPage)
            page['compare'] = serialise_location_comparison_page(location_comparison_pages)
            page['themes'] = []
            for theme in themes:
                serialised_theme = serialise_spotlight_theme(theme.specific)
                page['themes'].append(serialised_theme)

            return JsonResponse(page, safe=False)
        except IndexError:
            return JsonResponse({}, safe=False)


@require_http_methods(["GET"])
def dashboard_data_view(request):
    """
    Handles the /api/dashboard endpoint, fetching dashboard data from a private GitHub repo
    """
    GITHUB_REPO = 'devinit/org-dashboard-data'
    BRANCH_NAME = 'master'
    FILE = 'all.csv'

    try:
        g = Github(settings.GITHUB_TOKEN)

        repo = g.get_repo(GITHUB_REPO)
        branch = repo.get_branch(branch=BRANCH_NAME)
        contents = repo.get_contents(FILE, ref=branch.commit.sha)
        data = []
        with urllib.request.urlopen(contents.download_url) as response:
            with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
                shutil.copyfileobj(response, tmp_file)

                with open(tmp_file.name) as csvf:
                    csvReader = csv.reader(csvf)
                    header = next(csvReader)

                    for row in csvReader:
                        item = {
                            'department': row[0], 'metric': row[1], 'et': row[2], 'category': row[3],
                            'year': row[4], 'quarter': row[5], 'date': row[6], 'value': row[7],
                            'target': row[8], 'narrative': row[9], 'baseline': row[10]
                        }
                        data.append(item)

        return JsonResponse({ 'data': data }, safe=False)
    except Exception as e:
        if hasattr(e, 'message'):
            return JsonResponse({ 'error': e.message }, safe=False)

        return JsonResponse({ 'error': 'An error occurred' }, safe=False)
