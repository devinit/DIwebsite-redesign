import os
from django.conf import settings
from settings.models import PrimaryMenu

def globals(request):

    if request.path.startswith('/admin/') or request.path.startswith('/django-admin/'):
        return {}

    return {
        'global': {
            'DEBUG': bool(os.getenv('DEBUG', False)),
            'site_name': request.site.site_name or settings.WAGTAIL_SITE_NAME,
            'assets_root': '/assets',
            'primary_menu': construct_nav(PrimaryMenu.for_site(request.site).primary_menu_links.all()),
        },
    }


def construct_nav(qs):
    nav = list(qs)
    return nav
