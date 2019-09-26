import json

from django.conf import settings
from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.shortcuts import render

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin, TypesetBodyMixin
from .utils import create_new_ticket
from datetime import date
HONEYPOT_FORM_FIELD = 'captcha'
HS_TICKET_PREFIX = 'WS'


class ContactUs(models.Model):
    """
        Form fields for contact us form
    """
    name = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=255, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'organisation', 'email', 'telephone', 'message']


class ContactPage(TypesetBodyMixin, HeroMixin, Page):
    """
        Form with pre-built form fields to handle contact us info
    """
    template = 'contactus/contact_page.html'
    landing_template = 'contactus/contact_page_landing.html'

    success_alert = models.CharField(
        max_length=255,
        default='Your message was sent successfully',
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        FieldPanel('success_alert', classname="full"),
        InlinePanel('page_notifications', label='Notifications')
    ]

    class Meta():
        verbose_name = 'Contact Us Page'

    parent_page_types = ['home.HomePage']
    subpage_types = ['general.General']

    def render_landing_page(
            self,
            request,
            form_submission=None,
            *args,
            **kwargs):
        """
        Renders the landing page as used in wagtails default form implementation
        """
        context = self.get_context(request)
        context['form_submission'] = form_submission
        return render(
            request,
            self.landing_template,
            context
        )

    def generate_hubspot_object(self, form_object):

        today = date.today()
        subject = today.strftime("%Y%m%d")

        hubspot_payload = []
        kv_p = {}
        kv_p['name'] = 'subject'
        kv_p['value'] = HS_TICKET_PREFIX + subject
        hubspot_payload.append(kv_p)

        kv_p2 = {}
        kv_p2['name'] = 'hs_pipeline'
        kv_p2['value'] = settings.HS_TICKET_PIPELINE
        hubspot_payload.append(kv_p2)

        kv_p3 = {}
        kv_p3['name'] = 'hs_pipeline_stage'
        kv_p3['value'] = settings.HS_TICKET_PIPELINE_STAGE
        hubspot_payload.append(kv_p3)

        kv_p4 = {}
        kv_p4['name'] = 'client_first_name'
        kv_p4['value'] = form_object.get('name')
        hubspot_payload.append(kv_p4)

        kv_p5 = {}
        kv_p5['name'] = 'organisation'
        kv_p5['value'] = form_object.get('organisation')
        hubspot_payload.append(kv_p5)

        kv_p6 = {}
        kv_p6['name'] = 'email_address'
        kv_p6['value'] = form_object.get('email')
        hubspot_payload.append(kv_p6)

        kv_p7 = {}
        kv_p7['name'] = 'contact_details'
        kv_p7['value'] = form_object.get('telephone')
        hubspot_payload.append(kv_p7)

        kv_p8 = {}
        kv_p8['name'] = 'content'
        kv_p8['value'] = form_object.get('message')
        hubspot_payload.append(kv_p8)

        return hubspot_payload

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactUsForm(request.POST)

            """
                Check if hidden field has been filled by robots, if its filled; then its spam,
                return the default form page to be refilled
            """
            try:
                if request.POST.get(HONEYPOT_FORM_FIELD, '') != '':
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

            if form.is_valid():
                form_submission = form.save()

                hs_obj = self.generate_hubspot_object(request.POST)
                create_new_ticket(hs_obj)

                return self.render_landing_page(
                    request, form_submission, *args, **kwargs)
            else:
                context = self.get_context(request)
                context['form'] = form

                return render(
                    request,
                    self.get_template(request),
                    context
                )

        else:
            form = ContactUsForm()

            context = self.get_context(request)
            context['form'] = form

            return render(
                request,
                self.get_template(request),
                context
            )
