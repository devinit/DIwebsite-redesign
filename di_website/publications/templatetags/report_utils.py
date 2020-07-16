from django import template

register = template.Library()


@register.simple_tag
def get_previous_chapter(chapters, chapter_number):
    if not chapters and not chapter_number:
        return ''
    try:
        chapters = list(chapters)
        for index, item in enumerate(chapters):
            if int(item.chapter_number) == int(chapter_number):
                if index > 0:
                    return chapters[index - 1]
        return ''
    except Exception:
        return ''


@register.simple_tag
def get_next_chapter(chapters, chapter_number):
    if not chapters and not chapter_number:
        return ''
    try:
        chapters = list(chapters)
        for index, item in enumerate(chapters):
            if int(item.chapter_number) == int(chapter_number):
                if index < len(chapters) - 1:
                    return chapters[index + 1]
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
    try:
        for item in context['page'].content:
            if item.block.name == 'interactive_chart':
                return True
        return False
    except Exception:
        return False
