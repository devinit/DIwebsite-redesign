from django import template

register = template.Library()


@register.simple_tag
def get_featured_pages(page_blocks):
    featured_pages = [block.value for block in page_blocks if block.value.live]
    return featured_pages
