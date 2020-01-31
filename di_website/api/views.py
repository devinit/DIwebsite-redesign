import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from wagtail.core.models import Site

from di_website.home.templatetags.navigation_tags import get_menu_items
from di_website.home.templatetags.footer_tags import get_footer_text
from di_website.datasection.models import DataSectionPage
from .utils import (
    serialise_page,
    fetch_and_serialise_newsletters,
    fetch_and_serialise_footer_sections,
    serialise_spotlight_theme)
from di_website.spotlight.models import SpotlightPage
from di_website.spotlight.snippets import SpotlightTheme


@require_http_methods(["GET"])
def spotlights_navigation_view(request):
    """
    Handles the /api/spotlights/navigation/ endpoint, returning the navigation links (pri & seco)
    """
    navigation = {'primary': [], 'secondary': []}
    root_page = request.site.root_page
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
        page = serialise_page(request, spotlight, fields=['title', 'full_url'])
        meta = spotlight.meta
        page['themes'] = []
        if meta:
            themes = SpotlightTheme.objects.filter(spotlight=meta)
            for theme in themes:
                serialised_theme = serialise_spotlight_theme(theme)
                page['themes'].append(serialised_theme)
        pages.append(page)

    return JsonResponse(pages, safe=False)


@require_http_methods(["GET"])
def spotlight_page_view(request, slug=None):
    if slug:
        try:
            spotlight = SpotlightPage.objects.filter(slug=slug)[0]
            page = serialise_page(request, spotlight, fields=['title', 'full_url', 'country_code'])
            meta = spotlight.meta
            page['themes'] = []
            if meta:
                themes = SpotlightTheme.objects.filter(spotlight=meta)
                for theme in themes:
                    serialised_theme = serialise_spotlight_theme(theme)
                    page['themes'].append(serialised_theme)

            return JsonResponse(page, safe=False)
        except IndexError:
            return JsonResponse({}, safe=False)
