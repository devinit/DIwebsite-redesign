from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register('insert_global_admin_js')
def global_admin_js():
    return format_html(
        """
        <script>
            $(function() {{
                $('form[action^="/admin/documents/edit/"]').each(function() {{
                    $(this)
                        .find('.field.file_field.file_input')
                        .closest('li.required')
                        .each(function() {{
                            var message = '<li><p class="help-block help-info">To preserve the original filename of edited documents, upload and save the file twice in succession.</p></li>';
                            $(message).insertBefore(this);
                        }});
                }});

            }});
        </script>
        """
    )
