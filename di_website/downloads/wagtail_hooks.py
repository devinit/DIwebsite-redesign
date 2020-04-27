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
        <script>
            $().ready(function() {{
                function transformConfigElements() {{
                    $('.ace-editor-json-block textarea').each(function() {{
                        const textarea = this;
                        const aced = textarea.classList.contains('ace-editor-json-block-aced') || textarea.classList.contains('ace_text-input');
                        if (!aced) {{
                            textarea.style.display = 'none';
                            const aceElement = document.createElement('div');
                            aceElement.innerHTML = textarea.innerHTML;
                            aceElement.style.height = '400px';

                            const parent = textarea.parentNode;
                            parent.appendChild(aceElement);

                            const editor = ace.edit(aceElement);
                            editor.setTheme("ace/theme/monokai");
                            editor.session.setMode("ace/mode/json");

                            textarea.classList.add('ace-editor-json-block-aced');

                            editor.getSession().on('change', function() {{
                                textarea.innerHTML = editor.getSession().getValue();
                            }});
                        }}
                    }});
                }};

                transformConfigElements();

                $('.c-sf-add-button').each(function() {{
                    const button = this;
                    button.addEventListener('click', function() {{
                        window.setTimeout(function() {{
                            transformConfigElements();
                        }}, 500);
                    }});
                }});
            }});
        </script>
        """
    )
