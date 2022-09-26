from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.rich_text import DraftailRichTextArea


class FootnoteForm(forms.Form):
    text = forms.CharField(
        widget=DraftailRichTextArea,
        label=_('Text')
    )
    uuid = forms.CharField(
        widget=forms.HiddenInput()
    )
