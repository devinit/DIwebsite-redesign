from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from di_website.common.base import StandardPage


class AbstractLink(models.Model):
    class Meta:
        abstract = True

    label = models.CharField(
        max_length=255,
        blank=True
    )
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_url = models.URLField(blank=True)

    panels = [
        FieldPanel('label'),
        PageChooserPanel('page'),
        FieldPanel('link_url')
    ]


@register_snippet
class NewsLetter(models.Model):
    caption = models.CharField(
        max_length=255,
        default='Sign up for our newsletter to receive regular news and updates',
    )
    link_label = models.CharField(
        max_length=255,
        default='Subscribe here'
    )
    link_url = models.URLField(blank=True)

    panels = [
        FieldPanel('caption'),
        FieldPanel('link_label'),
        FieldPanel('link_url')
    ]

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'


@register_snippet
class FooterSection(Orderable, ClusterableModel):
    title = models.CharField(max_length=255)
    show_navigation_links = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        FieldPanel('show_navigation_links'),
        InlinePanel('footer_section_links', label='Section Links'),
        InlinePanel('footer_social_links', label='Social Links')
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Sections"



class FooterLink(Orderable, AbstractLink):
    section = ParentalKey('FooterSection', on_delete=models.CASCADE, related_name="footer_section_links")

    def __str__(self):
        return (self.page.title if self.page else self.label)

    class Meta:
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"


class SocialLink(Orderable, models.Model):
    SOCIAL_CHOICES = [
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
    ]

    social_platform = models.CharField(
        max_length=100,
        choices=SOCIAL_CHOICES
    )
    link_url = models.CharField(max_length=255, default='')
    section = ParentalKey('FooterSection', on_delete=models.CASCADE, related_name="footer_social_links")

    panels = [
        FieldPanel('social_platform'),
        FieldPanel('link_url')
    ]

    def __str__(self):
        return self.social_platform

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'


@register_snippet
class FooterText(models.Model):
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer Text"

    class Meta:
        verbose_name_plural = 'Footer Text'

class HomePage(StandardPage):
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Home Page'
