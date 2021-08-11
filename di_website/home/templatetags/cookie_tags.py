from django import template
from di_website.home.models import CookieNotice

register = template.Library()

@register.inclusion_tag('tags/cookie_notice.html', takes_context=True)
def cookie_notice(context):
    return {
        'notice': CookieNotice.objects.first(),
        'request': context['request'],
    }
