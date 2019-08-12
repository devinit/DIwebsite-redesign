from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField,AbstractFormSubmission
from di_website.common.mixins import HeroMixin
from di_website.common.base import hero_panels
from .utils import CustomFormBuilder

import json
from django.core.serializers.json import DjangoJSONEncoder

CAPTCHA_FORM_FIELD = 'captcha'


class CustomFormSubmission(AbstractFormSubmission):
    spam_post = models.BooleanField(default=False,)

class FormFields(AbstractFormField): 
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')


class ContactPage(HeroMixin,AbstractEmailForm):
    
    """ Override get_form to assign custom classes and attributes. Followed guide from 
        https://stackoverflow.com/questions/48321770/how-to-modify-attributes-of-the-wagtail-form-input-fields 
    """

    template = "contactus/contact_page.html"

    form_builder = CustomFormBuilder

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        hero_panels(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_submission_class(self):
        return CustomFormSubmission

    def process_form_submission(self, form):
       # form_data = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)
        self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
            page=self,
        )
    
    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)

            errors = form.errors.as_data()
            if form.is_valid():
                form_submission = self.process_form_submission(form)
                return self.render_landing_page(request, form_submission, *args, **kwargs)

        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form

        return render(
            request,
            self.get_template(request),
            context
        )

