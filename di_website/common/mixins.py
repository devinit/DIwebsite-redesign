from django.db import models

from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField, StreamField

from .blocks import BaseStreamBlock, SectionStreamBlock, TypesetStreamBlock


class HeroMixin(models.Model):
    class Meta:
        abstract = True

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Hero Image'
    )
    hero_image_credit_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Image credit name',
        help_text='Name of source of image used in hero if any'
    )
    hero_image_credit_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image credit url',
        help_text='A Link to the original source of the image if any'
    )
    hero_text = RichTextField(
        null=True,
        blank=True,
        help_text='A description of the page content'
    )
    hero_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero link',
        help_text='Choose a page to link to for the Call to Action'
    )
    hero_link_caption = models.CharField(
        max_length=255,
        blank=True,
        help_text='Text to display on the link button'
    )


class OtherPageMixin(Orderable):
    other_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Page',
        help_text='A page to link to in the "Other Pages or Related Links" section')

    class Meta():
        abstract = True


class BaseStreamBodyMixin(models.Model):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class TypesetBodyMixin(models.Model):
    body = StreamField(
        TypesetStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class SectionBodyMixin(models.Model):
    sections = StreamField(
        SectionStreamBlock(),
        verbose_name="Sections",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
