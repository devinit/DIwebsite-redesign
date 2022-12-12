from django import template

register = template.Library()

@register.simple_tag
def get_previous_page(all_pages, label):
    try:
        for index, item in enumerate(all_pages):
            if index > 0:
                if item.label == label:
                    return all_pages[index - 1]
        return ''
    except Exception:
        return ''


@register.simple_tag
def get_next_page(all_pages, label):
    try:
        for index, item in enumerate(all_pages):
            if index < len(all_pages) - 1:
                if item.label == label:
                    return all_pages[index + 1]

        return ''
    except Exception:
        return ''


@register.simple_tag
def chapter_nav_slice(chapters, chapter_number=0, max_length=6):
    try:
        zerod = chapter_number - 1 if chapter_number else 0
        length = len(chapters)
        max_from_end = max(length - max_length, 0)
        start = max_from_end if zerod > max_from_end else zerod
        end = zerod + max_length
        return '%s:%s' % (str(start), str(end))
    except Exception:
        return ''


@register.simple_tag(takes_context=True)
def page_contains_chart(context):
    charts = {'plotly_studio': False, 'advanced': False}
    self = context.get('page')
    try:
        content = self.tools if hasattr(self, 'tools') else self.content
        for item in content:
            if item.block.name == 'interactive_chart':
                charts['plotly_studio'] = True
            elif item.block.name == 'advanced_interactive_chart':
                charts['advanced'] = True

        return charts
    except Exception:
        return charts
