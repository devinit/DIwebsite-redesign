from django import template
from django.db import models
from itertools import chain
from di_website.blog.models import BlogArticlePage
from di_website.publications.models import AudioVisualMedia, LegacyPublicationPage, ShortPublicationPage, PublicationPage

register = template.Library()

def streamfield_index_query(field_name, value, index_count=3):
    """
    Generates an OR query for manually filtering through a list of streamfield values by checking each index
    """
    query = None
    for index in range(index_count):
        sub_query = models.Q(**{field_name + "__%s__value" % index: value})
        query = sub_query if not query else query | sub_query
    return query


@register.simple_tag
def user_content(author_page):
    """
    Blogs, Publications that were authored by the user
    """
    index_count = 5
    publications_query = streamfield_index_query('authors', author_page.pk, index_count)
    blog_query = streamfield_index_query('other_authors', author_page.pk, index_count)
    audio_visual_query = streamfield_index_query('participants', author_page.pk, index_count)

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
