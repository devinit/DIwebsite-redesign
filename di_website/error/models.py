from django.db import models

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel
)
from wagtail.core.models import Orderable, Page

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin, OtherPageMixin


class ErrorPage(BaseStreamBodyMixin, HeroMixin, Page):
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='Error Reporting Email'
    )
    contactus_url = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Contact Us URL'
    )
    home_url = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Home Page URL'
    )
    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        FieldPanel('email'),
        FieldPanel('contactus_url'),
        FieldPanel('home_url'),
    ]

    class Meta():
        verbose_name = 'Error Page'
