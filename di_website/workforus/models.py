from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel
)
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin
from .blocks import BenefitsStreamBlock

from modelcluster.fields import ParentalKey


class WorkForUsPage(BaseStreamBodyMixin, HeroMixin, Page):
    class Meta():
        verbose_name = 'Work For Us Page'

    recruitment_policy = models.URLField(
        null=True,
        blank=True,
        verbose_name='Recruitment Policy',
        help_text='A Link to the recruitment policy if any'
    )

    gdr_policy = models.URLField(
        null=True,
        blank=True,
        verbose_name='GDPR Policy',
        help_text='A Link to the GDPR policy if any'
    )

    benefits = StreamField(
        BenefitsStreamBlock,
        verbose_name="Benefits",
        null=True,
        blank=True
    )

    logos = StreamField(
        [('image', ImageChooserBlock())],
        verbose_name="Logos",
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        FieldPanel('recruitment_policy'),
        FieldPanel('gdr_policy'),
        StreamFieldPanel('benefits'),
        StreamFieldPanel('logos'),
    ]
