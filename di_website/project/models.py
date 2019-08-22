from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    InlinePanel,
    PageChooserPanel,
    MultiFieldPanel,
    FieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.core.blocks import (
    CharBlock,
    RichTextBlock,
    StructBlock,
    StreamBlock,
    TextBlock,
    URLBlock
)

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin, OtherPageMixin
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_RELATED_LINKS


class ProjectPage(BaseStreamBodyMixin, HeroMixin, Page):
    other_pages_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Section Title'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('project_related_links', label="Related links", max_num=MAX_RELATED_LINKS)
        ], heading='Other Pages')
    ]

    parent_page_types = [
        'FocusAreasPage'
    ]

    class Meta():
        verbose_name = 'Project Page'


class ProjectPageRelatedLink(OtherPageMixin):
    page = ParentalKey(
        Page,
        related_name='project_related_links',
        on_delete=models.CASCADE
    )
    panels = [
        PageChooserPanel('other_page')
    ]


class FocusAreasPage(BaseStreamBodyMixin, HeroMixin, Page):
    subpage_types = ['ProjectPage']

    class Meta():
        verbose_name = 'Focus Areas Page'

    parent_page_types = ['home.HomePage']

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            InlinePanel('focus_areas_page_link', label="Focus Areas Section", max_num=6)
        ], heading='Focus Areas'),
        InlinePanel('focus_areas_related_links', label="More About Section", max_num=4)
    ]


class FocusAreasPageLink(Orderable):
    page = ParentalKey(
        Page,
        related_name='focus_areas_page_link',
        on_delete=models.CASCADE
    )
    first_project_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='First Project Page',
        help_text='A page to link to projects in Focus Areas Section'
    )
    second_project_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Second Project Page',
        help_text='An extra page to link to projects in Focus Area Section'
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Title'
    )
    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Sub Title'
    )
    body = RichTextField(
        blank=True,
        null=True,
        help_text="Something about focus areas"
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Focus Area Image',
        help_text='Add an image to this focus area'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        ImageChooserPanel('image'),
        PageChooserPanel('first_project_page'),
        PageChooserPanel('second_project_page')
    ]


class FocusAreasPageRelatedLink(OtherPageMixin):
    page = ParentalKey(
        Page,
        related_name='focus_areas_related_links',
        on_delete=models.CASCADE
    )
    panels = [
        PageChooserPanel('other_page')
    ]
