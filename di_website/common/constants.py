MINIMAL_RICHTEXT_FEATURES = [
    'link',
    'footnote',
]
SIMPLE_RICHTEXT_FEATURES = [
    'bold',
    'italic',
    'ol',
    'ul',
    'link'
]
RICHTEXT_FEATURES = [
    'h2',
    'h3',
    'h4',
    'bold',
    'italic',
    'ol',
    'ul',
    'hr',
    'link',
    'document-link',
    'image',
    'embed',
    'anchor',
    'footnote'
]
MAX_RELATED_LINKS = 3
MAX_OTHER_PAGES = 4
MAX_PAGE_SIZE = 9

RICHTEXT_FEATURES_NO_FOOTNOTES = RICHTEXT_FEATURES.copy()
RICHTEXT_FEATURES_NO_FOOTNOTES.remove('footnote')

FOOTNOTE_RICHTEXT_FEATURES = [
    'footnote',
]
