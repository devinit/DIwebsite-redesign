from django import template
register = template.Library()


@register.filter
def placeholder(field, page):
    try:
        return page.get_placeholder_for_field(field)
    except Exception:
        return None

