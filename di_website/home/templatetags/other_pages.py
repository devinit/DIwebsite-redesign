from django import template

from wagtail.core.models import Page

register = template.Library()

"""
Get all the other pages that make up part of the menu
"""
@register.inclusion_tag('includes/cards/other_pages.html', takes_context=True)
def get_other_pages(context):
    
    # TODO Filter out the current page, root page and home page, 
    # TODO Also filter out child pages of the children of home page

    published_pages = Page.objects.live()
    return {
        'published_pages':published_pages
    }
