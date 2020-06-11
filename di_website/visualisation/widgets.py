from django.forms import HiddenInput, Media

from wagtail.admin.staticfiles import versioned_static


class AceEditorInput(HiddenInput):
    template_name = 'visualisation/widgets/ace-editor.html'

    def __init__(self, editor_options=None, **kwargs):
        self.editor_options = editor_options
        super().__init__(**kwargs)

    @property
    def media(self):
        return Media(
            js=[
                versioned_static('visualisation/widgets/ace-editor.js'),
                versioned_static('https://pagecdn.io/lib/ace/1.4.7/ace.js'),
                versioned_static('https://pagecdn.io/lib/ace/1.4.7/theme-monokai.js')
            ]
        )
