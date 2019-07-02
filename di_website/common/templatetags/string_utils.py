import bleach
import mimetypes
import re
import uuid
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import force_escape, stringfilter
from django.utils.text import slugify, Truncator
from wagtail.core.rich_text import expand_db_html, RichText
from content.fields import RichText as RichTextBlock

register = template.Library()

WYSIWYG_LIST = bleach.ALLOWED_TAGS + [
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'p',
    'img',
    'iframe',
    'figure',
    'figcaption',
    'cite',
    'blockquote',
    'pre',
    'table',
    'tr',
    'td',
    'th',
    'span',
    'sup',
    'sub',
    'code',
    'blockquote',
    'abbr',
]
MINIMAL_LIST = bleach.ALLOWED_TAGS + [
    'p',
]
ATTRS = bleach.ALLOWED_ATTRIBUTES
ATTRS['img'] = ['alt', 'src', 'class', 'width', 'height']
ATTRS['iframe'] = ['src', 'width', 'height', 'frameborder', 'title', 'webkitallowfullscreen', 'mozallowfullscreen', 'allowfullscreen']

# Allow style attribute on span
ATTRS['span'] = ['style']

# Allow class for cite on p
ATTRS['p'] = ['class']

# Allow style attribute on p
ATTRS['p'] = ['style']

# Allow title attribute on attr
ATTRS['abbr'] = ['title']

# Allow only text alignment and justification on styles
STYLES = ['text-decoration', 'text-align']

# Allow some table attributes
ATTRS['table'] = ['id', 'summary', 'title']
ATTRS['th'] = ['id', 'colspan', 'rowspan', 'width']
ATTRS['td'] = ['id', 'colspan', 'rowspan']


@register.filter(name='wysiwyg_tags')
def wysiwyg_tags(text):
    return mark_safe(bleach.clean(
        text,
        tags=WYSIWYG_LIST,
        attributes=ATTRS,
        styles=STYLES,
        strip=True,
        strip_comments=True
    ).replace('<p> </p>', ''))


@register.filter(name='minimal_tags')
def minimal_tags(text):
    return mark_safe(bleach.clean(
        text,
        tags=MINIMAL_LIST,
        attributes=bleach.ALLOWED_ATTRIBUTES,
        styles=[],
        strip=True,
        strip_comments=True
    ))


@register.filter(name='strip_tags')
def strip_tags(text):
    return mark_safe(bleach.clean(
        text,
        tags=[],
        attributes=[],
        styles=[],
        strip=True,
        strip_comments=True
    ))


@register.filter(name='unescape')
def unescape(text):
    return mark_safe(text.decode('string-escape'))


@register.filter
def rich_text(value):
    if isinstance(value, RichText):
        # passing a RichText value through the |richtext filter should have no effect
        return str(value)
    elif value is None:
        html = ''
    else:
        html = expand_db_html(value)

    return mark_safe(html)


@register.filter
def content(value):
    return wysiwyg_tags(rich_text(value))


def autop_function(value):
    """
    Convert line breaks into <p> and <br> in an intelligent fashion.
    Originally based on: http://photomatt.net/scripts/autop

    Ported directly from the Drupal _filter_autop() function:
    http://api.drupal.org/api/function/_filter_autop
    """

    # All block level tags
    block = '(?:table|thead|tfoot|caption|colgroup|tbody|tr|td|th|div|dl|dd|dt|ul|ol|li|pre|select|form|blockquote|address|p|h[1-6]|hr)'

    # Split at <pre>, <script>, <style> and </pre>, </script>, </style> tags.
    # We don't apply any processing to the contents of these tags to avoid messing
    # up code. We look for matched pairs and allow basic nesting. For example:
    # "processed <pre> ignored <script> ignored </script> ignored </pre> processed"
    chunks = re.split('(</?(?:pre|script|style|object)[^>]*>)', value)
    ignore = False
    ignoretag = ''
    output = ''

    for i, chunk in zip(range(len(chunks)), chunks):
        prev_ignore = ignore

        if i % 2:
            # Opening or closing tag?
            is_open = chunk[1] != '/'
            tag = re.split('[ >]', chunk[2 - is_open:], 2)[0]
            if not ignore:
                if is_open:
                    ignore = True
                    ignoretag = tag

            # Only allow a matching tag to close it.
            elif not is_open and ignoretag == tag:
                ignore = False
                ignoretag = ''

        elif not ignore:
            chunk = re.sub(r'\n*$', r'', chunk) + "\n\n"  # just to make things a little easier, pad the end
            chunk = re.sub(r'<br />\s*<br />', "\n\n", chunk)
            chunk = re.sub(r'(<' + block + '[^>]*>)', r"\n\1", chunk)  # Space things out a little
            chunk = re.sub(r'(</' + block + '>)', r"\1\n\n", chunk)  # Space things out a little
            chunk = re.sub(r"\n\n+", r"\n\n", chunk)  # take care of duplicates
            chunk = re.sub(r'\n?(.+?)(?:\n\s*|$)', r"<p>\1</p>\n", chunk)  # make paragraphs, including one at the end
            chunk = re.sub(r"<p>(<li.+?)</p>", r"\1", chunk)  # problem with nested lists
            chunk = re.sub(r'<p><blockquote([^>]*)>', r"<blockquote\1><p>", chunk)
            chunk = chunk.replace('</blockquote></p>', '</p></blockquote>')
            chunk = re.sub(r'<p>\s*</p>\n?', r'', chunk)  # under certain strange conditions it could create a P of entirely whitespace
            chunk = re.sub(r'<p>\s*(</?' + block + r'[^>]*>)', r"\1", chunk)
            chunk = re.sub(r'(</?' + block + r'[^>]*>)\s*</p>', r"\1", chunk)
            chunk = re.sub(r'(?<!<br />)\s*\n', "<br />\n", chunk)  # make line breaks
            chunk = re.sub(r'(</?' + block + r'[^>]*>)\s*<br />', r"\1", chunk)
            chunk = re.sub(r'<br />(\s*</?(?:p|li|div|th|pre|td|ul|ol)>)', r'\1', chunk)
            chunk = re.sub(r'&([^#])(?![A-Za-z0-9]{1,8};)', r'&amp;\1', chunk)

        # Extra (not ported from Drupal) to escape the contents of code blocks.
        code_start = re.search('^<code>', chunk)
        code_end = re.search(r'(.*?)<\/code>$', chunk)
        if prev_ignore and ignore:
            if code_start:
                chunk = re.sub('^<code>(.+)', r'\1', chunk)
            if code_end:
                chunk = re.sub(r'(.*?)<\/code>$', r'\1', chunk)
            chunk = chunk.replace('<\\/pre>', '</pre>')
            chunk = force_escape(chunk)
            if code_start:
                chunk = '<code>' + chunk
            if code_end:
                chunk += '</code>'

        output += chunk

    return output


@register.filter
def autop(value, autoescape=None):
    return mark_safe(autop_function(value))


autop.is_safe = True
autop.needs_autoescape = True
autop = stringfilter(autop)


@register.filter
def unslugify(value):
    return value.replace('-', ' ')


# Helper function to return untruncated stripped content
def return_all_content(content):
    return mark_safe(strip_tags(str(content))) if content else None


# Helper function for content_excerpt
def return_content(content):
    return mark_safe(Truncator(strip_tags(str(content))).words(30))


@register.filter
def content_excerpt(item):
    try:
        if item.excerpt != '':
            return item.excerpt
        else:
            return return_content(item.content)
    except AttributeError:
        try:
            return return_content(item.content)
        except AttributeError:
            return ''
    except TypeError:
        for block in item.content:
            if type(block.block) is RichTextBlock:
                return return_content(block.value.get(block.block_type))
        return ''


@register.filter
def cta_label(item, default=''):
    if item.cta_label:
        return item.cta_label
    return default


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


@register.filter
def splitlines(value):
    try:
        return value.splitlines()
    except Exception:
        return ''


@register.filter
def verbose_name(object):
    return object._meta.verbose_name


@register.simple_tag
def uid():
    return str(uuid.uuid4())[:6]


@register.simple_tag(takes_context=True)
def uid_url(context, obj):
    try:
        request = context['request']
        return '%s://%s/%s' % (request.scheme, request.get_host(), obj.uuid)
    except Exception:
        try:
            request = context['request']
            return '%s://%s%s' % (request.scheme, request.get_host(), obj.url)
        except Exception:
            return ''


@register.filter
def string_start(value, up_to_character='-'):
    return value.split(up_to_character)[0]


@register.filter
def lookup(d, key):
    return d[key]


@register.filter
def columns(thelist, n):
    """
    Break a list into ``n`` columns, filling up each row to the maximum equal
    length possible. For example::
        >>> l = range(10)
        >>> columns(l, 2)
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
        >>> columns(l, 3)
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
        >>> columns(l, 4)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
        >>> columns(l, 5)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
        >>> columns(l, 9)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [], [], [], []]
        # This filter will always return `n` columns, even if some are empty:
        >>> columns(range(2), 3)
        [[0], [1], []]
    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    list_len = len(thelist)
    split = list_len // n

    if list_len % n != 0:
        split += 1
    return [thelist[split * i:split * (i + 1)] for i in range(n)]


@register.simple_tag
def prepend_with_char(value, string, char='.'):
    if string:
        return '%s%s%s' % (string, char, value)
    return value


@register.simple_tag
def section_id(value, string):
    return prepend_with_char(value, string).replace('.', '-')


@register.simple_tag
def note_id(note_id, counter):
    if not note_id:
        return ''
    return '%s-%s-%s' % ('note', note_id, counter)


@register.simple_tag
def definition_id(def_id, term):
    if not def_id:
        return ''
    return '%s-%s' % (def_id, slugify(term))
