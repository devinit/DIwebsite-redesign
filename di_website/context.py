import os
from django.conf import settings


def globals(request):

    if request.path.startswith('/admin/') or request.path.startswith('/django-admin/'):
        return {}

    return {
        'global': {
            'DEBUG': bool(os.getenv('DEBUG', False)),
            'site_name': request.site.site_name or settings.WAGTAIL_SITE_NAME,
            'banner_srcs': 'width-460 460w',
            'duo_srcs': 'fill-400x250-c100 400w, fill-800x500-c100 800w',
            'large_image_srcs': 'fill-400x250 400w, fill-800x500 800w',
            'min_image_srcs': 'min-250x100 400w, min-500x200 800w',
            'sq_crop_srcs': 'fill-200x200-c100 780w, fill-400x400-c100 1000w, fill-800x800-c100 1350w',
            'sq_srcs': 'fill-600x600 780w, fill-700x700 1000w, fill-800x800 1350w',
            'large_hero_srcs': 'fill-1000x700 780w, fill-1350x700 1000w, fill-1800x700 1350w',
            'hero_srcs': 'fill-400x300-c100 1w, fill-500x280-c100 400w, fill-780x230-c100 500w, fill-1000x435-c100 780w, fill-1350x435-c100 1000w, fill-1800x430-c100 1350w',
            'card_srcs': 'fill-370x150 1w, fill-470x150 400w, fill-750x150 500w, fill-270x150 780w, fill-270x150 1000w, fill-385x150 1350w',
            'card_crop_srcs': 'fill-370x150-c100 1w, fill-470x150-c100 400w, fill-750x150-c100 500w, fill-270x150-c100 780w, fill-270x150-c100 1000w, fill-385x150-c100 1350w',
            'teaser_srcs': 'fill-360x150 1w, fill-460x150 400w, fill-740x200 500w, fill-350x400 780w, fill-475x400 1000w, fill-680x400 1350w',
            'teaser_crop_srcs': 'fill-360x150-c100 1w, fill-460x150-c100 400w, fill-740x200-c100 500w, fill-350x400-c100 780w, fill-475x400-c100 1000w, fill-680x400-c100 1350w',
            'summary_srcs': 'fill-360x150 1w, fill-460x150 400w, fill-740x200 500w, fill-350x320 780w, fill-475x320 1000w, fill-680x320 1350w',
            'featured_srcs': 'fill-370x200 1w, fill-470x200 400w, fill-750x200 500w, fill-400x350 780w, fill-555x350 1000w',
            'cta_srcs': 'max-370x200 1w, max-470x200 400w, max-750x200 500w, max-880x200 780w, fill-250x300 1000w',
            'report_srcs': 'fill-250x350 1w',
            'blog_srcs': 'fill-370x200 1w, fill-470x200 400w, fill-170x200 500w, fill-265x200 780w, fill-365x200 1000w',
            'chapter_srcs': 'fill-370x175 1w, fill-470x175 400w, fill-750x175 500w',
            'related_srcs': 'fill-370x175 1w, fill-470x175 400w, fill-750x175 500w, fill-265x230 780w, fill-180x250 1000w',
            'people_srcs': 'fill-150x200 1w, fill-190x200 400w, fill-300x200 500w, fill-170x200 780w, fill-190x200 1350w',
            'profile_srcs': 'width-300 300w, width-600 600w',
            'image_srcs': 'width-270 300w, width-370 400w, width-470 500w, width-750 780w, width-800 800w',
            'sub_teaser_srcs': 'width-370 370w, width-470 470w, width-750 750w, width-300 300w, width-350 350w, width-490 490w',
            'case_study_srcs': 'fill-330x250 1w, fill-430x250 400w, fill-710x250 500w, fill-740x250 780w',
            'blog_classname': 'BlogArticlePage',
            'dataset_classname': 'DatasetPage',
            'figure_classname': 'FigurePage',
            'publication_classnames': ['PublicationPage', 'ShortPublicationPage', 'LegacyPublicationPage'],
            'event_classname': 'EventPage',
            'news_classname': 'NewsStoryPage'
        },
    }
