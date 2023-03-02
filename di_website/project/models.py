from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    InlinePanel,
    PageChooserPanel,
    MultiFieldPanel,
    FieldPanel
)
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Orderable, Page
from wagtail.blocks import PageChooserBlock

from di_website.common.base import hero_panels, get_related_pages
from di_website.common.mixins import HeroMixin, OtherPageMixin, TypesetBodyMixin
from di_website.common.constants import ALT_MAX_RELATED_LINKS, MAX_RELATED_LINKS, RICHTEXT_FEATURES_NO_FOOTNOTES
from di_website.publications.models import AudioVisualMedia, LegacyPublicationPage, PublicationPage, ShortPublicationPage
from di_website.publications.mixins import PublishedDateMixin
from di_website.publications.utils import PublishedDatePanel


RELATED_CHOICES = (
    ('manual', 'Manual'),
    ('topic', 'Topic')
)

class FocusAreasPageLinkTopic(TaggedItemBase):
    content_object = ParentalKey('project.FocusAreasPageLink', blank=True, on_delete=models.CASCADE, related_name='focus_areas_page_link_topics')


class ProjectPageTopic(TaggedItemBase):
    content_object = ParentalKey('project.ProjectPage', blank=True, on_delete=models.CASCADE, related_name='project_page_topics')


class ProjectPage(PublishedDateMixin, TypesetBodyMixin, HeroMixin, Page):
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
    topics = ClusterTaggableManager(through=ProjectPageTopic, blank=True, verbose_name="Topics")
    content_panels = Page.content_panels + [
        hero_panels(),
        PublishedDatePanel(),
        FieldPanel('topics'),
        FieldPanel('body'),
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
    subpage_types = ['ProjectPage', 'general.General', 'FocusAreasPage']
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
        FieldPanel('body'),
        MultiFieldPanel([
            InlinePanel('focus_areas_page_link', label="Focus Areas", max_num=6)
        ], heading='Focus Areas'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related Page', max_num=4)
        ], heading='Related Pages'),
        InlinePanel('page_notifications', label='Notifications')
    ]


class FocusAreasPageLink(ClusterableModel):
    page = ParentalKey(
        Page,
        related_name='focus_areas_page_link',
        on_delete=models.CASCADE
    )
    projects = StreamField(
        [('page', PageChooserBlock(required=True))],
        verbose_name="Projects",
        null=True,
        blank=True,
        use_json_field=True
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
    related_page_section_title = models.CharField(blank=True, max_length=255, default='Key Projects and Publications', verbose_name='Section Title')
    related_page_handler = models.CharField(max_length=253, choices=RELATED_CHOICES, default='manual', verbose_name='Show By')
    topics = ClusterTaggableManager(through=FocusAreasPageLinkTopic, blank=True, verbose_name="Topics")
    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('image'),
        
        MultiFieldPanel([
            FieldPanel('related_page_section_title'),
            FieldPanel('related_page_handler', heading='Show by'),
            FieldPanel('topics', help_text="Fill in tags if you selected topics above"),
            FieldPanel('projects'),
        ], heading='Focus Area Pages', help_text="Displays only projects, publications, podcasts, blogs and news stories")
    ]

    def get_topic_related_pages(self):
        objects = {
            'audio': AudioVisualMedia.objects,
            'legacy': LegacyPublicationPage.objects,
            'publication': PublicationPage.objects,
            'short': ShortPublicationPage.objects,
            'project': ProjectPage.objects,
        }

        if self.related_page_handler == 'topic' or self.related_page_handler == 'Topic':
            combined_queryset = {}
            for key in objects:
                results = objects[key].live().filter(topics__in=self.topics.get_queryset()).order_by('title').distinct()
                for item in results:
                    if item.title:
                        combined_queryset[item.title] = item
            combined_queryset = self.remove_duplicates(combined_queryset)
            slice_queryset = combined_queryset[:ALT_MAX_RELATED_LINKS] if len(combined_queryset) > ALT_MAX_RELATED_LINKS else combined_queryset
            return get_related_pages(self, slice_queryset, objects, ALT_MAX_RELATED_LINKS)
    
    def remove_duplicates(self, queryset):
        unique_list = []
        for key in queryset.keys():
            unique_list.append(queryset[key])
        return unique_list


class FocusAreasProjects(OtherPageMixin):
    page = ParentalKey(
        Page,
        related_name='focus_areas_projects',
        on_delete=models.CASCADE
    )
    panels = [
        PageChooserPanel('other_page')
    ]
