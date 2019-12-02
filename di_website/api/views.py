import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from wagtail.core.models import Site

from di_website.home.templatetags.navigation_tags import get_menu_items
from di_website.datasection.models import DataSectionPage
from .utils import serialise_page


@require_http_methods(["GET"])
def spotlights_navigation_view(request):
    result = []
    root_page = request.site.root_page;
    data_section_page = DataSectionPage.objects.live().first()
    primary_menu_items = get_menu_items(root_page, data_section_page)
    navigation = {'primary': [], 'secondary': []}
    for menu_item in primary_menu_items:
        navigation['primary'].append(serialise_page(menu_item, request))
    if data_section_page:
        secondary_menu_items = get_menu_items(data_section_page, None) # FIXME: replace calling page with SpotlightsPage
        for menu_item in secondary_menu_items:
            navigation['secondary'].append(serialise_page(menu_item, request))

    result.append(navigation)

    return JsonResponse(result, safe=False)
