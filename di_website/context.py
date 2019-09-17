import os
from django.conf import settings


def globals(request):

    if request.path.startswith('/admin/') or request.path.startswith('/django-admin/'):
        return {}

    return {
        'global': {
            'DEBUG': bool(os.getenv('DEBUG', False)),
            'site_name': request.site.site_name or settings.WAGTAIL_SITE_NAME,
            'large_hero_srcs': 'fill-1000x700 780w, fill-1350x700 1000w, fill-1800x700 1350w',
            'hero_srcs': 'fill-400x200 1w, fill-500x280 400w, fill-780x230 500w, fill-1000x435 780w, fill-1350x435 1000w, fill-1800x430 1350w',
            'banner_srcs': 'fill-460x260 460w',
            'card_srcs': 'fill-370x150 1w, fill-470x150 400w, fill-750x150 500w, fill-270x150 780w, fill-270x150 1000w, fill-385x150 1350w',
            'image_srcs': 'width-270 300w, width-370 400w, width-470 500w, width-750 780w, width-750 780w, width-800 800w',
            'blog_classname': 'BlogArticlePage',
            'publication_classnames': ['PublicationPage', 'ShortPublicationPage', 'LegacyPublicationPage'],
            'event_classname': 'EventPage',
            'news_classname': 'NewsStoryPage'
        },
    }
