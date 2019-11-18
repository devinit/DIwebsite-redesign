import os
from django.conf import settings

from di_website.home.models import HomePage


def get_current_page(request):
    try:
        # this try is here to protect against 500 errors when there is a 404 error
        # taken from https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailcore/views.py#L17
        path_components = [component for component in request.path.split('/') if component]
        current_page, args, kwargs = request.site.root_page.specific.route(request, path_components)
        return current_page
    except Exception:
        return None


def get_html_title(request):
    current_page = get_current_page(request)
    # Try getting the page name in a format like:
    # Page title - Site title
    try:
        html_title = ''
        if current_page.seo_title:
            html_title += current_page.seo_title
        else:
            html_title += current_page.title
        if not isinstance(current_page, HomePage):
            html_title += ' - '
            html_title += str(request.site.site_name)
    except Exception:
        # Probably 404 or wagtail admin
        html_title = ''

    return html_title


def globals(request):

    if request.path.startswith('/admin/') or request.path.startswith('/django-admin/'):
        return {}

    html_title = get_html_title(request)
    current_page = get_current_page(request)
    is_home = isinstance(current_page, HomePage)

    return {
        'global': {
            'DEBUG': bool(os.getenv('DEBUG', False)),
            'is_home': is_home,
            'site_name': request.site.site_name or settings.WAGTAIL_SITE_NAME,
            'html_title': html_title,
            'large_hero_srcs': 'fill-1000x700 780w, fill-1350x700 1000w, fill-1800x700 1350w',
            'hero_srcs': 'fill-400x200 1w, fill-500x280 400w, fill-780x230 500w, fill-1000x435 780w, fill-1350x435 1000w, fill-1800x430 1350w',
            'banner_srcs': 'width-460 460w',
            'card_srcs': 'fill-370x150 1w, fill-470x150 400w, fill-750x150 500w, fill-270x150 780w, fill-270x150 1000w, fill-385x150 1350w',
            'image_srcs': 'width-270 300w, width-370 400w, width-470 500w, width-750 780w, width-750 780w, width-800 800w',
            'blog_classname': 'BlogArticlePage',
            'dataset_classname': 'DatasetPage',
            'figure_classname': 'FigurePage',
            'publication_classnames': ['PublicationPage', 'ShortPublicationPage', 'LegacyPublicationPage'],
            'event_classname': 'EventPage',
            'news_classname': 'NewsStoryPage'
        },
    }
