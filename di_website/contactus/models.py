from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from di_website.common.mixins import HeroMixin
from di_website.common.base import hero_panels
from di_website.contactus.utils import CustomFormBuilder

import json
from django.core.serializers.json import DjangoJSONEncoder

HONEYPOT_FORM_FIELD = 'captcha'


class FormFields(AbstractFormField): 
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')

    """
        Form fields with additional placeholder text that describes what the form fields are meant for
    """
    placeholder = models.CharField(
        blank=True,
        max_length=255,
        help_text='Optional placeholder for the field'
    )

    panels = AbstractFormField.panels + [
        FieldPanel('placeholder'),
    ]


class ContactPage(HeroMixin,AbstractEmailForm):
    """
        Contact Us form, to inherit the emailing functionality from wagtail, we'll use AbstractEmailForm
    """
    template = "contactus/contact_page.html"

    form_fields = CustomFormBuilder

    intro = RichTextField(blank=True)
    success_alert = models.CharField(
        max_length=255,
        default='Your message was sent successfully',
        )


    content_panels = AbstractEmailForm.content_panels + [
        hero_panels(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        
        FieldPanel('success_alert', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def process_form_submission(self, form):
       # form_data = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)
        self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
            page=self,
        )
        return form.cleaned_data

    def get_placeholder_for_field(self, label):
        try:
            return self.form_fields.filter(label=label).first().placeholder
        except RuntimeError:
            return None

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, request.FILES, page=self, user=request.user)
           
            """
                Check if hidden field has been filled by robots, if its filled; then its spam, 
                return the default form page to be refilled
            """
            try:
                if  form.data[HONEYPOT_FORM_FIELD] != '':
                    form = self.get_form(page=self, user=request.user)
                    context = self.get_context(request)
                    context['form'] = form

                    return render(
                        request,
                        self.get_template(request),
                        context
                    )
            except KeyError:
                # If honeypot fails, form should be marked as possible spam
                pass
            
            errors = form.errors.as_data()
            if form.is_valid():
                form_submission = self.process_form_submission(form)

                return self.render_landing_page(request, form_submission, *args, **kwargs)
            else:
                context = self.get_context(request)
                context['form'] = form

                return render(
                    request,
                    self.get_template(request),
                    context
                )

        else:
            form = self.get_form(page=self, user=request.user)

            context = self.get_context(request)
            context['form'] = form

            return render(
                request,
                self.get_template(request),
                context
            )

