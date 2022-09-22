from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks

@hooks.register('insert_global_admin_css')
def global_admin_css():
    """Add /static/css/admin.css to the admin."""
    return format_html('<link rel="stylesheet" href="{}">', static("css/admin.css"))

@hooks.register('before_copy_page')
def update_related_options_handler(request, page):
    """Update related_option_handler to uppercase"""
    page.specific.related_option_handler = page.specific.related_option_handler.upper()
    return page
