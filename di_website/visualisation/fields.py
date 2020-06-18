from django.forms import Media, widgets
from django.db import models
from django.contrib.postgres import fields

from wagtail.admin.staticfiles import versioned_static


class AceEditorInput(widgets.HiddenInput):
    template_name = 'visualisation/widgets/ace-editor.html'

    def __init__(self, editor_options=None, **kwargs):
        self.editor_options = editor_options
        super().__init__(**kwargs)

    @property
    def media(self):
        return Media(
            css = {
                'all': ('visualisation/widgets/css/ace-editor.css',)
            },
            js=[
                versioned_static('visualisation/widgets/js/ace-editor.js'),
                versioned_static('https://pagecdn.io/lib/ace/1.4.7/ace.js'),
                versioned_static('https://pagecdn.io/lib/ace/1.4.7/theme-monokai.js'),
                versioned_static('https://cdn.plot.ly/plotly-basic-latest.min.js') #TODO: import dynamically based on chart type
            ]
        )

class AceEditorField(fields.JSONField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': AceEditorInput}
        defaults.update(kwargs)
        return super().formfield(**defaults)
