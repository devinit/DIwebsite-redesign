from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.core.models import Orderable, Page
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey


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
class UsefulLink(AbstractLink):
    def __str__(self):
        return (self.page.title if self.page else self.label)

    class Meta:
        verbose_name = 'useful link'
        verbose_name_plural = 'useful links'


class PageFooterLink(Orderable, AbstractLink):
    related_page = ParentalKey('wagtailcore.Page', on_delete=models.CASCADE, related_name="footer_links")

    def __str__(self):
        return (self.page.title if self.page else self.label)

    class Meta:
        verbose_name = "footer link"
        verbose_name_plural = "footer links"


class StandardPage(Page):
    class Meta:
        abstract = True

    footer_links_title = models.CharField(
        max_length=255,
        blank=True,
        default=''
    )
    content_panels = Page.content_panels + [
        FieldPanel('footer_links_title'),
        InlinePanel('footer_links', label='Footer Links')
    ]


class HomePage(StandardPage):
    pass
