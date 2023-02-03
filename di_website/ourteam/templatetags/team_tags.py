from django import template
from itertools import chain
from di_website.blog.models import BlogArticlePage
from di_website.publications.models import AudioVisualMedia, LegacyPublicationPage, ShortPublicationPage, PublicationPage
from di_website.common.base import get_query
from di_website.common.constants import AUTHOR_INDEXES

register = template.Library()


@register.simple_tag
def user_content(author_page):
    """
    Blogs, Publications that were authored by the user
    """
    query = get_query(AUTHOR_INDEXES, 'authors', author_page.pk)
    blog_query = get_query(AUTHOR_INDEXES, 'other_authors', author_page.pk)
    audio_visual_query = get_query(AUTHOR_INDEXES, 'participants', author_page.pk)

    return sorted(list(chain(
        BlogArticlePage.objects.filter(internal_author_page=author_page).live().order_by('-published_date'),
        BlogArticlePage.objects.filter(blog_query).live().order_by('-published_date'),
        BlogArticlePage.objects.filter(blog_query).live(),
        PublicationPage.objects.filter(query).live(),
        ShortPublicationPage.objects.filter(query).live(),
        LegacyPublicationPage.objects.filter(query).live(),
        AudioVisualMedia.objects.filter(audio_visual_query).live(),
        # DatasetPage.objects.filter(authors__contains="\"value\": {},".format(author_page.pk)).live(),
        # DatasetPage.objects.filter(authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
    )), key=lambda content:content.published_date, reverse=True)
