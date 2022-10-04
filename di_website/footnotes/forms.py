from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.rich_text import DraftailRichTextArea

from di_website.common.constants import SIMPLE_RICHTEXT_FEATURES


class FootnoteForm(forms.Form):
    use_richtext = forms.BooleanField(required=False, initial=False, label=_('Use Rich Text'))
    text = forms.CharField(
        widget=DraftailRichTextArea(features=SIMPLE_RICHTEXT_FEATURES),
        label=_('Text')
    )
    uuid = forms.CharField(
        widget=forms.HiddenInput()
    )
