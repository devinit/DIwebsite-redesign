from django import template

from wagtail.core.models import Page

from di_website.home.models import (
    FooterLink,
    FooterText,
    FooterSection,
    NewsLetter,
    SocialLink
)
from di_website.home.templatetags.navigation_tags import get_menu_items

register = template.Library()


@register.inclusion_tag('includes/scaffold/useful_links.html', takes_context=True)
def get_footer_sections(context, parent, calling_page=None):
    footer_sections = FooterSection.objects.all()
    for footer_section in footer_sections:
        footer_section.links = footer_section.footer_section_links.all()

        footer_section.social_links = footer_section.footer_social_links.all()
        for social_link in footer_section.social_links:
            social_link.image_url = 'svg/source/' + social_link.social_platform + '.svg'

        if footer_section.show_navigation_links:
            footer_section.menu_items = get_menu_items(parent, calling_page)

    return {
        'footer_sections': footer_sections,
        'request': context['request'],
    }


@register.inclusion_tag('includes/scaffold/newsletter.html')
def subscribe_to_newsletter():
    return {
        'newsletters': NewsLetter.objects.all()
    }


@register.inclusion_tag('includes/scaffold/footer_text.html')
def get_footer_text():
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().body

    return {
        'footer_text': footer_text,
    }
