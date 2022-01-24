import json
from django.template import Context, Library, Template

register = Library()


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


@register.simple_tag(takes_context=True)
def load_as_template(context, raw_html=None):
    template = Template(raw_html)
    context = Context(context)

    return template.render(context)


@register.simple_tag(takes_context=True)
def has_pivot_table(context):
    context = Context(context)
    self = context['page']
    has_pivot_table = False
    for block in self.content:
        if block.block_type == 'pivot_table':
            has_pivot_table = True
            break

    return has_pivot_table
