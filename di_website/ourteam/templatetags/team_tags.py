from django import template
from django.db import models
from itertools import chain
from di_website.blog.models import BlogArticlePage
from di_website.publications.models import AudioVisualMedia, LegacyPublicationPage, ShortPublicationPage, PublicationPage

register = template.Library()

AUTHOR_INDEXES = [0,1,2,3,4]

def get_query(count_list, field_name, value):
    query = None
    for count in count_list:
        filter = models.Q(**{field_name + "__%s__value" % count: value})
        if not query:
            query = filter
        else:
            query = query | filter
    return query


@register.simple_tag
def user_content(author_page):
    """
    Blogs, Publications that were authored by the user
    """
    publications_query = get_query(AUTHOR_INDEXES, 'authors', author_page.pk)
    blog_query = get_query(AUTHOR_INDEXES, 'other_authors', author_page.pk)
    audio_visual_query = get_query(AUTHOR_INDEXES, 'participants', author_page.pk)

    return sorted(list(chain(
        BlogArticlePage.objects.filter(internal_author_page=author_page).live().order_by('-published_date'),
        BlogArticlePage.objects.filter(blog_query).live().order_by('-published_date'),
        PublicationPage.objects.filter(publications_query).live(),
        ShortPublicationPage.objects.filter(publications_query).live(),
        LegacyPublicationPage.objects.filter(publications_query).live(),
        AudioVisualMedia.objects.filter(audio_visual_query).live(),
        # DatasetPage.objects.filter(authors__contains="\"value\": {},".format(author_page.pk)).live(),
        # DatasetPage.objects.filter(authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
    )), key=lambda content:content.published_date, reverse=True)
