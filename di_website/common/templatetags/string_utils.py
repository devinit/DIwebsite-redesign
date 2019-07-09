import uuid

from django import template

register = template.Library()

@register.simple_tag
def uid():
    return str(uuid.uuid4())[:6]
