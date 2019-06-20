from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    pass


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
