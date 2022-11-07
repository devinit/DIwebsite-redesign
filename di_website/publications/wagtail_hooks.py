import json

from django.conf import settings
from django.template import loader
from django.templatetags.static import static
from django.utils.html import escape, format_html, format_html_join
from django.utils.safestring import mark_safe

from draftjs_exporter.dom import DOM

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
from wagtail.admin.ui.components import Component
from wagtail import hooks
from wagtail.whitelist import allow_without_attributes, attribute_rule


@hooks.register('register_rich_text_features')
def register_anchor_feature(features):
    """Register the `anchor` feature, which uses the `ANCHOR` Draft.js entity type, and is stored as HTML with a `<span>` tag."""
    features.default_features.append('anchor')
    feature_name = 'anchor'
    type_ = 'ANCHOR'

    control = {
        'type': type_,
        'label': '#',
        'description': 'Anchor',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(control, js=['common/js/anchor.js'])
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'span[data-type="anchor"]': AnchorEntityElementHandler(type_)},
        'to_database_format': {'entity_decorators': {type_: anchor_entity_decorator}},
    })


def anchor_entity_decorator(props):
    """Draft.js ContentState to database HTML.
    Converts the ANCHOR entities into an a tag.
    """
    return DOM.create_element('span', { "data-id": props['id'], "data-type": 'anchor' }, props['children'])


class AnchorEntityElementHandler(InlineEntityElementHandler):
    """Database HTML to Draft.js ContentState.
    Converts the div tag into an ANCHOR entity, with the right data.
    """

    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        """Take the ``data-anchor`` value from the ``data-anchor`` HTML attribute."""
        return {
            'id': attrs['data-id'],
        }


class WelcomePanel(Component):
    order = 50

    def render_html(self, parent_context):
        template = loader.get_template('wagtailadmin/welcome_panel.html')
        return template.render({})


def to_js_primitive(string):
    return mark_safe(json.dumps(escape(string)))


@hooks.register('construct_homepage_panels')
def register_welcome_panel(request, panels):
    return panels.append(WelcomePanel())


@hooks.register('insert_editor_css')
def editor_css():

    # Any extra CSS for customising the page editor can be added here as well
    return format_html('<link rel="stylesheet" href="{}">', static("css/editor.css"))


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'span': attribute_rule({'style': True}),
        'p': attribute_rule({'style': True}),
        'sup': allow_without_attributes,
        'sub': allow_without_attributes,
        'code': allow_without_attributes,
        'blockquote': allow_without_attributes,
        'abbr': attribute_rule({'title': True}),
    }


@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script>
            $('body.create.model-personpage').each(function() {{
                $(function(e) {{
                    if ($('#id_slug').val() == '') {{
                        $('#id_slug').val('placeholder');
                    }}
                }});
            }});
            $('body.page-editor').each(function() {{
                $(function(e) {{
                    $('#id_uuid').closest('.object.char_field').hide();
                }});
            }});
            $(function() {{

                var taxonomyList = $('ul#id_language, ul#id_event_type');
                taxonomyList.find('label:contains("---------")')
                    .contents()
                    .filter(function() {{
                        return this.nodeType == 3
                    }}).each(function() {{
                        this.textContent = this.textContent.replace('---------', 'None');
                    }});
            }});
        </script>
        """
    )
