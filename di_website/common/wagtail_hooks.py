from django.templatetags.static import static
from draftjs_exporter.dom import DOM

from django.utils.html import format_html
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
import wagtail.admin.rich_text.editors.draftail.features as draftail_features

from wagtail.core import hooks

@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add /static/css/admin.css to the admin."""
    return format_html('<link rel="stylesheet" href="{}">', static("css/admin.css"))

@hooks.register('register_rich_text_features')
def register_non_modal_link_feature(features):
    """Register the `non-modal-link` feature, which uses the `NONMODALLINK` Draft.js entity type, and is stored as HTML with a `<a href>` tag."""
    features.default_features.append('non-modal-link')
    feature_name = 'non-modal-link'
    type_ = 'NONMODALLINK'

    control = {
        'type': type_,
        'icon': 'link',
        'description': 'Non-modal link',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(control, js=['common/js/non-modal-link.js'])
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'a[href]': NonModalLinkEntityElementHandler(type_)},
        'to_database_format': {'entity_decorators': {type_: non_modal_link_entity_decorator}},
    })


def non_modal_link_entity_decorator(props):
    """Draft.js ContentState to database HTML.
    Converts the NONMODALLINK entities into an a tag.
    """
    return DOM.create_element('a', { 'href': props['href'] }, props['children'])


class NonModalLinkEntityElementHandler(InlineEntityElementHandler):
    """Database HTML to Draft.js ContentState.
    Converts the a tag into an NONMODALLINK entity, with the right data.
    """

    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        """Take the ``href`` value from the ``href`` HTML attribute."""
        return {
            'href': attrs['href'],
        }
