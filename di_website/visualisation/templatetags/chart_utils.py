import json
from django import template

register = template.Library()


@register.filter
def as_json(value):
    try:
        return json.dumps(value)
    except Exception:
        return 'Invalid JSON data'
