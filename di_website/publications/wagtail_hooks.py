import json
from django.template import loader
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from wagtail.core import hooks
from wagtail.core.whitelist import allow_without_attributes, attribute_rule
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
from draftjs_exporter.dom import DOM
from django.utils.html import format_html_join
from django.conf import settings


@hooks.register('register_rich_text_features')
def register_anchor_feature(features):
    """Register the `anchor` feature, which uses the `ANCHOR` Draft.js entity type, and is stored as HTML with a `<a href>` tag."""
    features.default_features.append('anchor')
    feature_name = 'anchor'
    type_ = 'ANCHOR'

    control = {
        'type': type_,
        'label': '#',
        'description': 'Anchor link',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'a[href]': AnchorEntityElementHandler(type_)},
        'to_database_format': {'entity_decorators': {type_: anchor_entity_decorator}},
    })


def anchor_entity_decorator(props):
    """Draft.js ContentState to database HTML.
    Converts the ANCHOR entities into an a tag.
    """
    return DOM.create_element('a', {
        'href': props['href'],
    }, props['children'])


class AnchorEntityElementHandler(InlineEntityElementHandler):
    """Database HTML to Draft.js ContentState.
    Converts the a tag into an ANCHOR entity, with the right data.
    """

    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        """Take the ``href`` value from the ``href`` HTML attribute."""
        return {
            'href': attrs['href'],
        }


@hooks.register('insert_editor_js')
def anchor_editor_js():
    """Include some extra javascript in the editor."""
    js_files = [
        'wagtailadmin/js/draftail.js',
        'common/js/anchor.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>', ((settings.STATIC_URL, filename) for filename in js_files))
    return js_includes


class WelcomePanel(object):
    order = 50

    def render(self):
        template = loader.get_template('wagtailadmin/welcome_panel.html')
        return template.render({})


def to_js_primitive(string):
    return mark_safe(json.dumps(escape(string)))


@hooks.register('construct_homepage_panels')
def register_welcome_panel(request, panels):
    return panels.append(WelcomePanel())


@hooks.register('insert_editor_css')
def editor_css():

    # For the data-text selector, see https://css-tricks.com/snippets/css/prevent-long-urls-from-breaking-out-of-container/
    # This fixes long URLs breaking the interface
    return format_html(
        """
        <style>

            body.page-editor.model-personpage button.action-preview {{
                display: none;
            }}

            .model_choice_field.radio_select label,
            .model_multiple_choice_field.radio_select label,
            .model_multiple_choice_field.checkbox_select_multiple label,
            #id_display_state label {{
                display: block;
                float: none;
                width: 100%;
            }}

            .page-editor .multiple .field-col,
            .page-editor .multiple .field-content,
            .page-editor .sequence-container .field-col,
            .page-editor .sequence-container .field-content
            {{
                float: none;
            }}

            .page-editor .multiple label,
            .page-editor .sequence-container label,
            .page-editor .custom__itemlist .sequence-container
            {{
                width: 100%;
            }}

            .page-editor .sequence-container .stream-menu-inner ul
            {{
                text-align: center;
            }}

            .page-editor .sequence-container .stream-menu-inner ul li
            {{
                display: inline-block;
                float: none;
            }}

            .page-editor .sequence-container .stream-menu li {{
                width: auto;
            }}

            .page-editor .sequence-container [data-text="true"] {{
                overflow-wrap: break-word;
                word-wrap: break-word;
                -ms-word-break: break-all;
                word-break: break-all;
                word-break: break-word;
                -ms-hyphens: auto;
                -moz-hyphens: auto;
                -webkit-hyphens: auto;
                hyphens: auto;
            }}

            .struct-block .fields .button-block .fields {{
                border-bottom: 1px solid #e6e6e6;
            }}

        </style>
        """
    )


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
