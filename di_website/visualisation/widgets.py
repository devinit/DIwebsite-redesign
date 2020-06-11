from django.forms import HiddenInput


class AceEditorInput(HiddenInput):
    template_name = 'visualisation/widgets/ace-editor.html'

    def __init__(self, editor_options=None, **kwargs):
        self.editor_options = editor_options
        super().__init__(**kwargs)
