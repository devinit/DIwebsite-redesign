from django.db import models

from wagtail.core.models import Orderable, Page

from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel
)

from wagtail.images.edit_handlers import ImageChooserPanel

"""
Most pages have a hero section, StandardPage defines contents of hero that can be inherited by other pages that need it
"""
class StandardPage(Page):
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

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            FieldPanel('hero_text', classname="hero_excerpt"),
            MultiFieldPanel([
                FieldPanel('hero_link_caption'),
                PageChooserPanel('hero_link')
            ])
        ], heading="Hero Section"),
    ]

