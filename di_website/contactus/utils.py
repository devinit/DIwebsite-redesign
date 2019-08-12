from django import forms
from wagtail.contrib.forms.forms import FormBuilder

class CustomFormBuilder(FormBuilder):
    
    @property
    def formfields(self):
        fields = super().formfields

        fields['name'] = forms.CharField()
        fields['organisation'] = forms.CharField()
        fields['email'] = forms.EmailField()
        fields['phone'] = forms.CharField(required=False)
        fields['message'] = forms.CharField()

        return fields

