"""
    Holds the custom template tags responsible for rendering the navigation menu
"""

from django import template

from wagtail.core.models import Page, Site

from di_website.context import globals

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    if 'request' in context.__dict__:
        return Site.find_for_request(context['request']).root_page
    return None


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


def has_children(page):
    return page.get_children().live().exists()


def is_active(page, current_page):
    return current_page.url_path.startswith(page.url_path) if current_page else False


def get_menu_items(page, calling_page):
    if (hasattr(page, 'get_children')):
        menu_items = page.get_children().live().in_menu()
        for menu_item in menu_items:
            menu_item.active = is_active(menu_item, calling_page)
        return menu_items

    return []


@register.inclusion_tag('tags/navigation/primary.html', takes_context=True)
def primary_menu(context, parent, calling_page=None):
    menu_items = get_menu_items(parent, calling_page)
    return {
        'calling_page': calling_page,
        'menu_items': menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context.get('request'),
    }


@register.inclusion_tag('tags/navigation/secondary.html', takes_context=True)
def secondary_menu(context, parent, calling_page=None):
    """
    Returns the children of the specified menu
    """
    global_obj = globals(context['request'])
    secondary_menu_items = get_menu_items(parent, calling_page)
    for menu_item in secondary_menu_items:
        menu_item.has_dropdown = has_menu_children(menu_item)
        menu_item.children = menu_item.get_children().live().in_menu()
    return {
        'parent': parent,
        'menu_items': secondary_menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context.get('request'),
        'global': global_obj['global']
    }


@register.inclusion_tag('tags/navigation/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    global_obj = globals(context['request'])
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.live().ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
        'global': global_obj['global']
    }
