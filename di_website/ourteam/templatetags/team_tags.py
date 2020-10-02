from django import template
from itertools import chain
from di_website.blog.models import BlogArticlePage
from di_website.publications.models import AudioVisualMedia, LegacyPublicationPage, ShortPublicationPage, PublicationPage
# from di_website.datasection.models import DatasetPage

register = template.Library()


@register.simple_tag
def user_content(author_page):
    """
    Blogs, Publications that were authored by the user
    """
    return list(chain(
        BlogArticlePage.objects.filter(internal_author_page=author_page).live(),
        BlogArticlePage.objects.filter(other_authors__contains="\"value\": {},".format(author_page.pk)).live(),
        BlogArticlePage.objects.filter(other_authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
        PublicationPage.objects.filter(authors__contains="\"value\": {},".format(author_page.pk)).live(),
        PublicationPage.objects.filter(authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
        ShortPublicationPage.objects.filter(authors__contains="\"value\": {},".format(author_page.pk)).live(),
        ShortPublicationPage.objects.filter(authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
        LegacyPublicationPage.objects.filter(authors__contains="\"value\": {},".format(author_page.pk)).live(),
        LegacyPublicationPage.objects.filter(authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
        AudioVisualMedia.objects.filter(participants__contains="\"value\": {},".format(author_page.pk)).live(),
        AudioVisualMedia.objects.filter(participants__contains="\"value\": {}}}".format(author_page.pk)).live(),
        # DatasetPage.objects.filter(authors__contains="\"value\": {},".format(author_page.pk)).live(),
        # DatasetPage.objects.filter(authors__contains="\"value\": {}}}".format(author_page.pk)).live(),
    ))
