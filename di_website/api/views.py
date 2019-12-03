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
    fetch_and_serialise_footer_sections)


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
        navigation['primary'].append(serialise_page(menu_item, request))
    if data_section_page:
        secondary_menu_items = get_menu_items(data_section_page, None) # FIXME: replace calling page with SpotlightsPage
        for menu_item in secondary_menu_items:
            navigation['secondary'].append(serialise_page(menu_item, request))

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
