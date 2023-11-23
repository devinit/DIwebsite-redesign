from django import template

register = template.Library()


@register.simple_tag
def get_featured_pages(page_blocks):
    featured_pages = [block.value for block in page_blocks if block.value.live]
    ordered_featured_pages = sorted(featured_pages, key=lambda x:
                                    getattr(x.specific, 'publication_date',getattr(x.specific, 'first_published_at', None)), reverse=True)
    return ordered_featured_pages
