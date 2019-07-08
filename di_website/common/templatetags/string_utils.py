import uuid
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import force_escape, stringfilter
from django.utils.text import slugify, Truncator
from wagtail.core.rich_text import expand_db_html, RichText
from wagtail.core.blocks import  RichTextBlock

register = template.Library()

@register.simple_tag
def uid():
    return str(uuid.uuid4())[:6]
