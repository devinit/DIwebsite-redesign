from django import template

from wagtail.core.models import Page

from di_website.home.models import CommunicationLink, FooterText, NewsLetter, SocialLink, UsefulLink

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

def get_menu_items(page, calling_page):
    menu_items = page.get_children().live().in_menu()
    for menu_item in menu_items:
        menu_item.active = is_active(menu_item, calling_page)
    return menu_items

@register.inclusion_tag('includes/navigation/primary.html', takes_context=True)
def primary_menu(context, parent, calling_page=None):
    menu_items = get_menu_items(parent, calling_page)
    return {
        'calling_page': calling_page,
        'menu_items': menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('includes/scaffold/useful_links.html', takes_context=True)
def get_useful_links(context, parent, calling_page=None):
    menu_items = get_menu_items(parent, calling_page)
    other_links = UsefulLink.objects.all()
    return {
        'title': 'Useful Links',
        'calling_page': calling_page,
        'menu_items': menu_items,
        'other_links': other_links,
        'request': context['request'],
    }


@register.inclusion_tag('includes/scaffold/newsletter.html', takes_context=True)
def subscribe_to_newsletter(context):
    return { 'newsletters': NewsLetter.objects.all() }


@register.inclusion_tag('includes/scaffold/useful_links.html', takes_context=True)
def get_page_footer_links(context, parent, calling_page=None):
    footer_links = parent.footer_links.all()
    title = parent.specific.footer_links_title
    if (calling_page and calling_page.footer_links.first()):
        footer_links = calling_page.footer_links.all()
        title = calling_page.specific.footer_links_title

    return {
        'title': title,
        'other_links': footer_links,
        'calling_page': calling_page,
        'request': context['request'],
    }


@register.inclusion_tag('includes/scaffold/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().body

    return {
        'footer_text': footer_text,
    }

@register.inclusion_tag('includes/scaffold/useful_links.html', takes_context=True)
def get_communication_links(context):
    other_links = CommunicationLink.objects.all()
    social_links = SocialLink.objects.all()
    for social_link in social_links:
        social_link.image_url = 'svg/source/' + social_link.label + '.svg'
    return {
        'title': 'Get in Touch',
        'other_links': other_links,
        'social_links': social_links,
        'request': context['request'],
    }
