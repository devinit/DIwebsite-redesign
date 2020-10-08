from django.forms import Media, widgets
from django.db import models
from django.contrib.postgres.fields import JSONField

from wagtail.admin.staticfiles import versioned_static


class AceEditorInput(widgets.HiddenInput):
    template_name = 'visualisation/widgets/ace-editor.html'

    def __init__(self, options=None, **kwargs):
        self.options = options
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
                # versioned_static('https://cdn.plot.ly/plotly-basic-latest.min.js')
            ]
        )


    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['options'] = self.options
        return context

class AceEditorJSONField(JSONField):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {'mode': 'json'})
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        options = self.options
        options.mode = 'json'
        defaults = {'widget': AceEditorInput(options=options)}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class AceEditorField(models.TextField):
    """
    Handles any data type e.g. HTML, CSS, JavaScript
    """
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {'mode': 'json'})
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': AceEditorInput(options=self.options)}
        defaults.update(kwargs)
        return super().formfield(**defaults)
