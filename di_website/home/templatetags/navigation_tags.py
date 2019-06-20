from django import template

from wagtail.core.models import Page

from di_website.home.models import NewsLetter

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


def has_children(page):
    return page.get_children().live().exists()


def is_active(page, current_page):
    return (current_page.url_path.startswith(page.url_path) if current_page else False)

@register.inclusion_tag('includes/navigation/primary.html', takes_context=True)
def primary_menu(context, parent, calling_page=None):
    menu_items = parent.get_children().live().in_menu()
    for menu_item in menu_items:
        menu_item.active = is_active(menu_item, calling_page)
    return {
        'calling_page': calling_page,
        'menu_items': menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('includes/scaffold/newsletter.html', takes_context=True)
def subscribe_to_newsletter(context):
    return { 'newsletters': NewsLetter.objects.all() }
