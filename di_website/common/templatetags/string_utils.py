import uuid
import mimetypes

from django import template

register = template.Library()

@register.simple_tag
def uid():
    return str(uuid.uuid4())[:6]


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)


@register.filter
def file_info(file):
    try:
        return '%s %s' % (mimetypes.guess_extension(mimetypes.guess_type(file.url)[0])[1:].upper(), sizeof_fmt(file.file.size))
    except Exception:
        return file.title


@register.filter
def file_label(file):
    try:
        return '%s | %s %s' % (
            file.title,
            mimetypes.guess_extension(mimetypes.guess_type(file.url)[0])[1:].upper(),
            sizeof_fmt(file.file.size)
        )
    except Exception:
        return file.title
