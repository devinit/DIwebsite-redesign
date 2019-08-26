from django import template
from di_website.workforus.models import Values

register = template.Library()


# Our values snippets
@register.inclusion_tag('tags/cards/our_values.html', takes_context=True)
def values(context):
    return {
        'values': Values.objects.all(),
        'request': context['request'],
    }
