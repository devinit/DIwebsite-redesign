from draftjs_exporter.dom import DOM
from django.conf.urls import include, url
from django.utils.html import format_html_join
from django.templatetags.static import static
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
from wagtail.core import hooks
from di_website.footnotes import urls

ICON_PATH = ['M846.857 600c34.857 20 46.857 65.143 26.857 100l-36.571 62.857c-20 34.857-65.143 46.857-100 26.857l-152-87.429v175.429c0 40-33.143 73.143-73.143 73.143h-73.143c-40 0-73.143-33.143-73.143-73.143v-175.429l-152 87.429c-34.857 20-80 8-100-26.857l-36.571-62.857c-20-34.857-8-80 26.857-100l152-88-152-88c-34.857-20-46.857-65.143-26.857-100l36.571-62.857c20-34.857 65.143-46.857 100-26.857l152 87.429v-175.429c0-40 33.143-73.143 73.143-73.143h73.143c40 0 73.143 33.143 73.143 73.143v175.429l152-87.429c34.857-20 80-8 100 26.857l36.571 62.857c20 34.857 8 80-26.857 100l-152 88z']


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^footnotes/', include(urls, namespace='footnotes')),
    ]


def footnote_entity_decorator(props):
    """
    Draft.js ContentState to database HTML.
    Converts the FOOTNOTE entities into a span tag.
    """
    return DOM.create_element('span', {
        'data-footnote': props['text'],
        'data-type': 'footnote',
        'data-id': props['uuid'],
    }, props['text'])


class FootnoteEntityElementHandler(InlineEntityElementHandler):
    """
    Database HTML to Draft.js ContentState.
    Converts the span tag into a FOOTNOTE entity, with the right data.
    """
    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        """
        Take the ``text`` value from the ``data-footnote`` HTML attribute.
        """
        return {
            'text': attrs['data-footnote'],
            'uuid': attrs['data-id'],
        }


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'footnotes/js/custom-vendor.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}"></script>', ((static(filename),) for filename in js_files))
    return js_includes


@hooks.register('register_rich_text_features')
def register_footnote_feature(features):
    features.default_features.append('footnote')
    """
    Registering the `footnote` feature, which uses the `FOOTNOTE` Draft.js entity type,
    and is stored as HTML with a `<span data-footnote>` tag.
    """
    feature_name = 'footnote'
    type_ = 'FOOTNOTE'

    control = {
        'type': type_,
        'icon': ICON_PATH,
        'description': 'Footnote',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(
            control,
            js=['footnotes/js/custom-admin.js'],
            css={'all': ['footnotes/css/footnotes.css']}
        )
    )

    features.register_converter_rule('contentstate', feature_name, {
        # Note here that the conversion is more complicated than for blocks and inline styles.
        'from_database_format': {'span[data-footnote]': FootnoteEntityElementHandler(type_)},
        'to_database_format': {'entity_decorators': {type_: footnote_entity_decorator}},
    })
