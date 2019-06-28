"""
    Holds the custom template tags responsible for rendering the navigation menu
"""

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


def has_children(page):
    return page.get_children().live().exists()


def is_active(page, current_page):
    return current_page.url_path.startswith(page.url_path) if current_page else False

def get_menu_items(page, calling_page):
    menu_items = page.get_children().live().in_menu()
    for menu_item in menu_items:
        menu_item.active = is_active(menu_item, calling_page)
    return menu_items

@register.inclusion_tag('tags/navigation/primary.html', takes_context=True)
def primary_menu(context, parent, calling_page=None):
    menu_items = get_menu_items(parent, calling_page)
    return {
        'calling_page': calling_page,
        'menu_items': menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register.inclusion_tag('tags/navigation/secondary.html', takes_context=True)
def secondary_menu(context, parent, calling_page=None):
    """
    Returns the children of the specified menu
    """
    secondary_menu_items = parent.get_children().live().in_menu()
    for menu_item in secondary_menu_items:
        menu_item.has_dropdown = has_menu_children(menu_item)
        menu_item.active = is_active(menu_item, calling_page)
        menu_item.children = menu_item.get_children().live().in_menu()
    return {
        'parent': parent,
        'menu_items': secondary_menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
