import json
from django import template

register = template.Library()


@register.filter
def as_json(value):
    try:
        return json.dumps(value)
    except Exception:
        return 'Invalid JSON data'


@register.filter
def padding_by_ratio(image):
    try:
        ratio = image.height / image.width
        return 'padding-top: %s%%;' % round(ratio * 100, 2)
    except Exception:
        return ''
