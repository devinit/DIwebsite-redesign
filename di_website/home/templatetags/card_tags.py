from django import template

from wagtail.core.models import Page


register = template.Library()


@register.inclusion_tag('tags/cards/other_pages.html', takes_context=True)
def get_other_pages(context, calling_page=None):
    """
    Get all the other pages that make up part of the menu
    """
    root_page = context.request.site.root_page.get_root()
    home_excludes = root_page.get_descendants(inclusive=True).filter(depth__lte=4) #  Root=1, Home=2, Homechild=3, Homegrandchild=4
    exclude_pks = [desc_page.pk for desc_page in home_excludes]

    if calling_page:
        exclude_pks.append(calling_page.pk)

    published_pages = Page.objects.live().exclude(pk__in=exclude_pks).specific()
    return {
        'published_pages': published_pages
    }
