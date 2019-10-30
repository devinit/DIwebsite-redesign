from django import forms
from django.utils.translation import ugettext_lazy as _


class FootnoteForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea,
        label=_('Text')
    )
    uuid = forms.CharField(
        widget=forms.HiddenInput()
    )
