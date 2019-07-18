from django import template


register = template.Library()


@register.inclusion_tag('tags/cards/other_pages.html', takes_context=True)
def get_other_pages(context, calling_page=None, heading='Other pages in this section'):
    """
    Get all the other pages
    """
    if calling_page:
        other_pages = [page.other_page.specific for page in calling_page.other_pages.all() if page.other_page.live]

    return {
        'heading': calling_page.other_pages_heading if hasattr(calling_page, 'other_pages_heading') else heading,
        'other_pages': other_pages,
        'request': context['request']
    }
