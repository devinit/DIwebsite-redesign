from django import forms
from wagtail.contrib.forms.forms import FormBuilder


class CustomFormBuilder(FormBuilder):
    
    @property
    def formfields(self):
        fields = super().formfields

        fields['captcha'] = forms.CharField()

        return fields

