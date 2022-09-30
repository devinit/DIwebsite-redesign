from django.templatetags.static import static
from draftjs_exporter.dom import DOM

from django.utils.html import format_html
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
import wagtail.admin.rich_text.editors.draftail.features as draftail_features

from wagtail.core import hooks

ICON_PATH = ['M104.41,6.1c6.26,5.13,6.93,11.83,7.62,13.46l0.34,2.5c0.9,5.39-1.65,12.75-5.58,17.38L89.2,59.84 c-6.76,7.84-18.04,10.44-27.48,6.37l-0.03,0.04c3.45,5.63,3.15,9.64,3.46,10.57c0.9,5.41-1.65,12.74-5.58,17.38L41.97,114.6 c-8.53,9.89-23.58,11.1-33.53,2.61c-5.04-5.04-7.84-9.31-8.37-16.49c-0.47-6.24,1.53-12.37,5.59-17.18l17.92-20.79 c5.01-5.14,7.5-5.86,13.33-7.47l2.5-0.34l10.66,1.56c0.22,0.08,0.44,0.18,0.65,0.27l0.03-0.04c-5.35-8.71-4.57-20.11,2.14-27.97 L70.48,8.37c4.11-4.77,9.99-7.71,16.15-8.19c5.37-0.89,12.77,1.64,17.38,5.58L104.41,6.1L104.41,6.1z M74.23,51.71l-3.66,4.24 l0.64,0.01l0.02,0l0.6-0.02l0.01,0l0.14-0.01l0.02,0c2.11-0.16,4.19-0.88,5.96-2.14c0.34-0.24,0.68-0.51,1.02-0.82l0,0l0,0 c0.3-0.27,0.62-0.59,0.93-0.95l0,0l0.12-0.13l17.45-20.24c1.47-1.7,2.36-3.75,2.68-5.86c0.07-0.44,0.11-0.87,0.13-1.26 c0.02-0.41,0.01-0.85-0.01-1.28l0-0.05l-0.01-0.11c-0.16-2.11-0.88-4.19-2.14-5.96c-0.24-0.34-0.51-0.67-0.78-0.97l-0.03-0.04 c-0.29-0.32-0.61-0.64-0.94-0.94l0,0l-0.06-0.05l-0.05-0.05L96.16,15c-1.69-1.43-3.7-2.3-5.78-2.61l-0.03,0 c-0.43-0.06-0.85-0.11-1.24-0.12c-0.41-0.02-0.84-0.01-1.27,0.01l-0.07,0l-0.1,0.01c-2.11,0.16-4.19,0.88-5.96,2.14 c-0.34,0.24-0.68,0.51-0.98,0.78l-0.03,0.03c-0.33,0.29-0.64,0.61-0.94,0.95l0,0l-0.12,0.13L62.2,36.55 c-1.47,1.7-2.36,3.75-2.68,5.86h0c-0.06,0.43-0.11,0.86-0.12,1.26c-0.02,0.41-0.01,0.85,0.01,1.28l0.01,0.15l0,0.01v0.02 c0.03,0.46,0.09,0.91,0.18,1.37l3.58-4.15l0.1-0.12l0.13-0.14l0,0l0.02-0.02c1.29-1.39,3.02-2.18,4.79-2.3 c1.78-0.13,3.62,0.39,5.1,1.6l0,0l0.02,0.01l0.09,0.08l0.02,0.02l0.02,0.02l0.01,0.01l0.02,0.01l0.07,0.06l0,0l0,0 c2.06,1.83,2.82,4.6,2.21,7.13c-0.12,0.5-0.3,1-0.54,1.48c-0.22,0.46-0.51,0.9-0.83,1.31l-0.02,0.02l-0.03,0.04l0,0l-0.01,0.02 l-0.1,0.12l0,0L74.23,51.71L74.23,51.71z M40.06,80.23L40.06,80.23c2.33,2.01,5.88,1.75,7.89-0.58l5.58-6.47 c0.65,1.45,1.04,3,1.16,4.57c0.25,3.44-0.79,6.97-3.19,9.75l-17.46,20.24c-2.4,2.79-5.73,4.34-9.16,4.59 c-3.38,0.25-6.84-0.75-9.59-3.05l-0.16-0.14c-2.78-2.4-4.34-5.73-4.59-9.16c-0.25-3.4,0.76-6.89,3.1-9.65l0.09-0.1l17.25-20l0,0 l0,0l0.21-0.24c2.4-2.78,5.73-4.34,9.16-4.59c1.58-0.12,3.18,0.04,4.71,0.47l-5.58,6.47C37.47,74.67,37.73,78.22,40.06,80.23 L40.06,80.23z']

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
