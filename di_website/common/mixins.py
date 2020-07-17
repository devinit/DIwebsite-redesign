from django.db import models

from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField, StreamField

from .blocks import BaseStreamBlock, SectionStreamBlock, TypesetStreamBlock, TypesetFootnoteStreamBlock
from .constants import RICHTEXT_FEATURES_NO_FOOTNOTES

from wagtailmetadata.models import MetadataPageMixin


class CustomMetadataPageMixin(MetadataPageMixin):

    class Meta:
        abstract = True

    def get_meta_image(self):
        if getattr(self.specific, 'search_image', None):
            return self.specific.search_image
        elif getattr(self.specific, 'hero_image', None):
            return self.specific.hero_image
        return super(CustomMetadataPageMixin, self).get_meta_image()

    def get_meta_description(self):
        return self.search_description if self.search_description else self.title

    def get_meta_title(self):
        return self.title


class HeroMixin(CustomMetadataPageMixin, models.Model):
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
    hero_image_credit_name = models.TextField(
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
        help_text='A description of the page content',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
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

    class Meta(Orderable.Meta):
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


class TypesetBodyFootnoteMixin(models.Model):
    body = StreamField(
        TypesetFootnoteStreamBlock(),
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


class CallToActionMixin(models.Model):
    call_to_action_title = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="Optional: when left blank, the call to action will not be show",
        verbose_name='Title'
    )
    call_to_action_body = models.TextField(
        null=True, blank=True, verbose_name='Description',
        help_text='Optional: describe the purpose of your call to action in a bit more detail')
    call_to_action_button_text = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Button caption',
        help_text='Optional: this is required to show the button')
    call_to_action_button_url = models.URLField(
        max_length=255, null=True, blank=True, verbose_name='Button URL',
        help_text='Optional: this is required to show the button')

    class Meta:
        abstract = True
