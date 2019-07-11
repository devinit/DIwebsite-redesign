from django import template
from wagtail.core.models import Page

register = template.Library()


@register.simple_tag
def user_owned_pages(user):
    return Page.objects.filter(owner=user).live()
