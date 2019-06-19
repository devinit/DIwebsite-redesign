import os
from django.conf import settings

def globals(request):

    if request.path.startswith('/admin/') or request.path.startswith('/django-admin/'):
        return {}

    return {
        'global': {
            'DEBUG': bool(os.getenv('DEBUG', False)),
            'site_name': request.site.site_name or settings.WAGTAIL_SITE_NAME,
            'assets_root': '/assets',
        },
    }
