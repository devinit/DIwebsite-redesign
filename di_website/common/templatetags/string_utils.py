import os

import bleach
import uuid
import re
import html

from bleach.css_sanitizer import CSSSanitizer
from urllib.parse import urlparse
from urllib.parse import parse_qs

from django import template
from django.utils import formats
from django.utils.encoding import punycode
from django.utils.text import Truncator, slugify
from django.utils.html import (
    escape, strip_tags, smart_urlquote, word_split_re, simple_url_re, simple_url_2_re,
    WRAPPING_PUNCTUATION, TRAILING_PUNCTUATION_CHARS)
from django.utils.safestring import SafeData, mark_safe
from django.template.base import VariableDoesNotExist

from wagtail.rich_text import expand_db_html, RichText

from di_website.publications.fields import RichText as RichTextBlock

register = template.Library()

WYSIWYG_LIST = bleach.ALLOWED_TAGS + [
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'hr',
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
ATTRS['span'] = ['style', 'data-type', 'data-id']

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

css_sanitizer = CSSSanitizer(allowed_css_properties=STYLES)

@register.filter(name='wysiwyg_tags')
def wysiwyg_tags(text):
    clean = bleach.clean(
        text,
        tags=WYSIWYG_LIST,
        attributes=ATTRS,
        css_sanitizer=css_sanitizer,
        strip=True,
        strip_comments=True
    )

    return mark_safe(re.sub(r'<p>\s*</p>', '', clean))


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


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)


@register.filter
def file_info(file):
    try:
        return '%s %s' % (os.path.splitext(file.url)[1][1:].upper(), sizeof_fmt(file.file.size))
    except Exception:
        return file.title


@register.filter
def file_label(file):
    try:
        return '%s | %s %s' % (
            file.title,
            os.path.splitext(file.url)[1][1:].upper(),
            sizeof_fmt(file.file.size)
        )
    except Exception:
        return file.title


@register.filter
def file_exists(file):
    try:
        if file.size:
            return True
    except:
        return False


@register.filter(expects_localtime=True, is_safe=False)
def format_date(start, end=None):
    """Check that years are not the same and format date field."""

    if start in (None, '') or end in (None, ''):
        return ''

    if formats.date_format(start, 'Y') == formats.date_format(end, 'Y'):
        return formats.date_format(start, "d F") + " - " + formats.date_format(end, "d F, Y")
    else:
        return formats.date_format(start, "d F, Y") + " - " + formats.date_format(end, "d F, Y")


# Helper function for content_excerpt
@register.filter
def return_content(content):
    return mark_safe(Truncator(strip_tags(str(content))).words(30))


@register.filter
def content_excerpt(item):
    if hasattr(item, "hero_text"):
        if item.hero_text != '':
            return return_content(item.hero_text)
    if hasattr(item, "content"):
        try:
            for block in item.content:
                if isinstance(block.block, RichTextBlock):
                    return return_content(block.value.get(block.block_type))
        except (AttributeError, VariableDoesNotExist, TypeError) as err:
            pass
    return ''


@register.filter
def string_start(value, up_to_character='-'):
    return value.split(up_to_character)[0]


@register.simple_tag
def prepend_with_char(value, string, char='.'):
    if string:
        return '%s%s%s' % (string, char, value)
    return value


@register.simple_tag
def section_id(value, string):
    return prepend_with_char(value, string).replace('.', '-')


@register.simple_tag
def definition_id(def_id, term):
    if not def_id:
        return ''
    return '%s-%s' % (def_id, slugify(term))


@register.filter
def add_string(stringA, stringB):
    """concatenate stringA & stringB"""
    return str(stringA) + str(stringB)

@register.filter
def buzzsprout_container_id(buzzsprout_url):
    """extract container id from buzzsprout embed URL"""
    parsed_url = urlparse(buzzsprout_url)
    container_ids = parse_qs(parsed_url.query).get('container_id', [])
    if len(container_ids) > 0:
        return container_ids[0]
    else:
        return ""


@register.filter
def markdownify_urls(text):
    """
    NB: This code is a modified version of the urlize method of django.utils.html

    Convert any URLs in text into markdown links format.

    Works on http://, https://, www. links, and also on links ending in one of
    the original seven gTLDs (.com, .edu, .gov, .int, .mil, .net, and .org).
    Links can have trailing punctuation (periods, commas, close-parens) and
    leading punctuation (opening parens) and it'll still do the right thing.
    """
    safe_input = isinstance(text, SafeData)

    def trim_punctuation(lead, middle, trail):
        """
        Trim trailing and wrapping punctuation from `middle`. Return the items
        of the new state.
        """
        # Continue trimming until middle remains unchanged.
        trimmed_something = True
        while trimmed_something:
            trimmed_something = False
            # Trim wrapping punctuation.
            for opening, closing in WRAPPING_PUNCTUATION:
                if middle.startswith(opening):
                    middle = middle[len(opening):]
                    lead += opening
                    trimmed_something = True
                # Keep parentheses at the end only if they're balanced.
                if (middle.endswith(closing) and
                        middle.count(closing) == middle.count(opening) + 1):
                    middle = middle[:-len(closing)]
                    trail = closing + trail
                    trimmed_something = True
            # Trim trailing punctuation (after trimming wrapping punctuation,
            # as encoded entities contain ';'). Unescape entities to avoid
            # breaking them by removing ';'.
            middle_unescaped = html.unescape(middle)
            stripped = middle_unescaped.rstrip(TRAILING_PUNCTUATION_CHARS)
            if middle_unescaped != stripped:
                trail = middle[len(stripped):] + trail
                middle = middle[:len(stripped) - len(middle_unescaped)]
                trimmed_something = True
        return lead, middle, trail

    def is_email_simple(value):
        """Return True if value looks like an email address."""
        # An @ must be in the middle of the value.
        if '@' not in value or value.startswith('@') or value.endswith('@'):
            return False
        try:
            p1, p2 = value.split('@')
        except ValueError:
            # value contains more than one @.
            return False
        # Dot must be in p2 (e.g. example.com)
        if '.' not in p2 or p2.startswith('.'):
            return False
        return True

    words = word_split_re.split(str(text))
    for i, word in enumerate(words):
        if '.' in word or '@' in word or ':' in word:
            # lead: Current punctuation trimmed from the beginning of the word.
            # middle: Current state of the word.
            # trail: Current punctuation trimmed from the end of the word.
            lead, middle, trail = '', word, ''
            # Deal with punctuation.
            lead, middle, trail = trim_punctuation(lead, middle, trail)

            # Make URL we want to point to.
            url = None
            if simple_url_re.match(middle):
                url = smart_urlquote(html.unescape(middle))
            elif simple_url_2_re.match(middle):
                url = smart_urlquote('http://%s' % html.unescape(middle))
            elif ':' not in middle and is_email_simple(middle):
                local, domain = middle.rsplit('@', 1)
                try:
                    domain = punycode(domain)
                except UnicodeError:
                    continue
                url = 'mailto:%s@%s' % (local, domain)

            # Make link.
            if url:
                middle = '[%s](%s)' % (escape(url), middle)
                words[i] = mark_safe('%s%s%s' % (lead, middle, trail))
            else:
                if safe_input:
                    words[i] = mark_safe(word)
        elif safe_input:
            words[i] = mark_safe(word)
    return ''.join(words)
