from django.utils.functional import cached_property
from django.forms import CharField

from wagtail.core.blocks import FieldBlock

from .widgets import AceEditorInput


class ChartBlock(FieldBlock):

    def __init__(self, *args, **kwargs):
        super(ChartBlock, self).__init__(*args, **kwargs)

    @cached_property
    def field(self):
        return CharField(widget=AceEditorInput(editor_options={}))
