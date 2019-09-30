from django.db import models
from django.utils.text import slugify

from wagtail.core.blocks import (
    CharBlock,
    RichTextBlock,
    StructBlock,
)
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from di_website.common.mixins import HeroMixin, TypesetBodyMixin, OtherPageMixin
from di_website.common.base import hero_panels, get_related_pages
from .blocks import ExpertiseBlock, FocusAreasBlock, LocationsMapBlock
from di_website.common.blocks import (
    BannerBlock, SectionStreamBlock, TestimonialBlock, VideoDuoTextBlock)
from di_website.common.constants import MAX_OTHER_PAGES
from di_website.news.models import NewsStoryPage

class WhatWeDoPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/07-what-we-do
    """

    class Meta:
        verbose_name = 'What We Do Page'

    sections = StreamField([
        ('locations_map', LocationsMapBlock()),
        ('focus_area', FocusAreasBlock()),
        ('expertise', ExpertiseBlock()),
        ('banner', BannerBlock()),
        ('duo', VideoDuoTextBlock()),
        ('testimonial', TestimonialBlock())
    ], verbose_name="Sections", null=True, blank=True)
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages', max_num=MAX_OTHER_PAGES)
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = [
        'project.FocusAreasPage',
        'whatwedo.ServicesPage',
        'news.NewsIndexPage',
        'events.EventIndexPage',
        'place.PlacesPage',
        'general.General'
    ]
    parent_page_types = ['home.HomePage']


@register_snippet
class ExampleTopic(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        help_text="Optional. Will be auto-generated from name if left blank.")

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ExampleTopic, self).save(*args, **kwargs)


class ServicesPageRelatedExample(OtherPageMixin):
    page = ParentalKey(
        'whatwedo.ServicesPage',
        related_name='services_related_example',
        on_delete=models.CASCADE)
    topics = models.ForeignKey(
        ExampleTopic, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)

    panels = [
        PageChooserPanel('other_page'),  # TODO: Are these meant to be project pages?
        SnippetChooserPanel('topics')
    ]


class ServicesPage(TypesetBodyMixin, HeroMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/09-consultancy-services
    """

    def get_context(self, request):
        context = super(ServicesPage, self).get_context(request)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            examples = ServicesPageRelatedExample.objects.filter(topics__slug=topic_filter)
        else:
            examples = ServicesPageRelatedExample.objects.all()

        context['topics'] = ExampleTopic.objects.all()
        context['selected_topic'] = topic_filter
        context['examples'] = examples
        context['related_news'] = get_related_pages(
            self.services_related_news.all(), NewsStoryPage.objects, min_len=0)

        return context

    contact_text = models.CharField(
        blank=True, null=True, max_length=250,
        default='Find out more about our consultancy services and what we can do for you')
    contact_button_text = models.CharField(
        blank=True, null=True, max_length=100, default='Get in touch')
    contact_email = models.EmailField(blank=True, null=True)

    specialities = StreamField([
        ('speciality', StructBlock([
            ('image', ImageChooserBlock(required=False)),
            ('heading', CharBlock(required=False)),
            ('body', RichTextBlock(required=False))
        ]))
    ])

    skills = StreamField([
        ('skill', StructBlock([
            ('heading', CharBlock(required=False)),
            ('body', RichTextBlock(required=False))
        ]))
    ])

    sections = StreamField(
        SectionStreamBlock(),
        verbose_name="Sections",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Services Page'

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            FieldPanel('contact_text'),
            FieldPanel('contact_button_text'),
            FieldPanel('contact_email')
        ], heading='Contact aside'),
        StreamFieldPanel('body'),
        StreamFieldPanel('specialities'),
        StreamFieldPanel('skills'),
        InlinePanel('services_related_news', label="Related news"),
        InlinePanel('services_related_example', label="Project examples"),
        StreamFieldPanel('sections'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['general.General']
    parent_page_types = [WhatWeDoPage]


class ServicesPageRelatedNews(OtherPageMixin):
    page = ParentalKey(ServicesPage, related_name='services_related_news', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', ['news.NewsStoryPage'])
    ]
