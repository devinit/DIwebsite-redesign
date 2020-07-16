from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        """
        <style>

            .help-block.help-info.no-padding-top {{
                margin-top: -46px;
            }}

        </style>
        """
    )
