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
from wagtail.core.blocks import PageChooserBlock

from di_website.common.base import hero_panels, get_related_pages
from di_website.common.mixins import HeroMixin, OtherPageMixin, TypesetBodyMixin
from di_website.common.constants import MAX_RELATED_LINKS, RICHTEXT_FEATURES_NO_FOOTNOTES


class ProjectPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/08-1-project
    """
    other_pages_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Section Title',
        default='Related content'
    )
    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('project_related_links', label="Related link", max_num=MAX_RELATED_LINKS)
        ], heading='Other Pages'),
        InlinePanel('page_notifications', label='Notifications')
    ]
    subpage_types = ['general.General']
    parent_page_types = [
        'FocusAreasPage'
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['related_pages'] = get_related_pages(self, self.project_related_links.all())

        return context

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


class FocusAreasPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/08-focus-areas
    """
    subpage_types = ['ProjectPage', 'general.General']
    parent_page_types = ['whatwedo.WhatWeDoPage']

    class Meta():
        verbose_name = 'Focus Areas Page'

    other_pages_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Section Title',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            InlinePanel('focus_areas_page_link', label="Focus Areas", max_num=6)
        ], heading='Focus Areas'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related Page', max_num=4)
        ], heading='Related Pages'),
        InlinePanel('page_notifications', label='Notifications')
    ]


class FocusAreasPageLink(Orderable):
    page = ParentalKey(
        Page,
        related_name='focus_areas_page_link',
        on_delete=models.CASCADE
    )
    projects = StreamField(
        [('page', PageChooserBlock(page_type="project.ProjectPage", required=True))],
        verbose_name="Projects",
        null=True,
        blank=True
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
        help_text="Something about focus areas",
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Image',
        help_text='Add an image to this focus area'
    )
    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        ImageChooserPanel('image'),
        StreamFieldPanel('projects')
    ]


class FocusAreasProjects(OtherPageMixin):
    page = ParentalKey(
        Page,
        related_name='focus_areas_projects',
        on_delete=models.CASCADE
    )
    panels = [
        PageChooserPanel('other_page')
    ]
