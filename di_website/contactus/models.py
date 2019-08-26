import json

from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.shortcuts import render

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin

HONEYPOT_FORM_FIELD = 'captcha'


class ContactUs(models.Model):
    """
        Form fields for contact us form
    """
    name = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'organisation', 'email', 'telephone', 'message']


class ContactPage(HeroMixin, Page):
    """
        Form with pre-built form fields to handle contact us info
    """
    template = 'contactus/contact_page.html'
    landing_template = 'contactus/contact_page_landing.html'

    intro = RichTextField(blank=True)
    success_alert = models.CharField(
        max_length=255,
        default='Your message was sent successfully',
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('intro', classname="full"),
        FieldPanel('success_alert', classname="full"),
    ]

    class Meta():
        verbose_name = 'Contact Us Page'

    parent_page_types = ['home.HomePage']

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

                # TODO Post content of form submission to hubspot CRM

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
