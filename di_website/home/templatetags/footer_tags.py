from django import template

from di_website.home.models import (
    FooterLink,
    FooterText,
    FooterSection,
    NewsLetter,
    SocialLink
)
from di_website.home.templatetags.navigation_tags import get_menu_items

from di_website.context import globals

register = template.Library()


@register.inclusion_tag('tags/footer/useful_links.html', takes_context=True)
def get_footer_sections(context, parent, calling_page=None):
    global_obj = globals(context['request'])
    footer_sections = FooterSection.objects.all()
    for footer_section in footer_sections:
        footer_section.links = footer_section.footer_section_links.all().order_by('sort_order')

        footer_section.social_links = footer_section.footer_social_links.all().order_by('sort_order')
        for social_link in footer_section.social_links:
            social_link.image_url = 'svg/source/' + social_link.social_platform + '.svg'

        if footer_section.show_navigation_links:
            footer_section.menu_items = get_menu_items(parent, calling_page)

    return {
        'footer_sections': footer_sections,
        'request': context.get('request'),
        'global': global_obj['global']
    }


@register.inclusion_tag('tags/footer/newsletter.html')
def subscribe_to_newsletter():
    return {
        'newsletters': NewsLetter.objects.all()
    }


@register.inclusion_tag('tags/footer/footer_text.html')
def get_footer_text():
    footer_text = ''
    footer_text_major = ''
    footer = FooterText.objects.first()
    if footer is not None:
        footer_text = footer.body
        footer_text_major = footer.major_content

    return {
        'footer_text': footer_text,
        'footer_text_major': footer_text_major
    }
