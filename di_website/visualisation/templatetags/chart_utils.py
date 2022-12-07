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

@register.simple_tag(takes_context=True)
def load_viz_assets(context, source='header'):
    context = Context(context)
    self = context['page']
    assets = []
    try:
        content = self.tools if hasattr(self, 'tools') else self.content
        for block in content:
            if block.block_type == 'advanced_interactive_chart':
                chart_page = block.value['chart_page']
                if chart_page and source == 'header':
                    header_assets = chart_page.specific.header_assets
                    duplicate = False
                    for asset in assets:
                        if asset == header_assets:
                            duplicate = True

                    if not duplicate:
                        assets.append(header_assets)
                elif chart_page and source == 'footer':
                    footer_assets = chart_page.specific.footer_assets
                    duplicate = False
                    for asset in assets:
                        if asset == footer_assets:
                            duplicate = True

                    if not duplicate:
                        assets.append(footer_assets)

        return load_as_template(context, '\n'.join(assets))
    except AttributeError:
        return ''

@register.simple_tag(takes_context=True)
def gets_row_highlights(context, pivot_page):
    highlights = []
    for highlight in pivot_page.row_highlights.all():
        highlights.append({
                "field": highlight.row_highlight_field,
                "condition": highlight.row_highlight_condition,
                "value": highlight.row_highlight_value,
                "color": highlight.row_highlight_colour or '#ffb3b3'
                })
    return json.dumps(highlights)
