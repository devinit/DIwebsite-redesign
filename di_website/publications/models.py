from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from di_website.common.base import hero_panels, get_paginator_range
from di_website.common.mixins import HeroMixin
from di_website.common.constants import MAX_PAGE_SIZE

from taggit.models import Tag, TaggedItemBase

from .mixins import FlexibleContentMixin
from .utils import ContentPanel


class PublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.PublicationPage', on_delete=models.CASCADE, related_name='publication_topics')


@register_snippet
class PublicationCountry(ClusterableModel):
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
        super(PublicationCountry, self).save(*args, **kwargs)


class PublicationIndexPage(HeroMixin, Page):

    content_panels = Page.content_panels + [
        hero_panels()
    ]

    subpage_types = ['PublicationPage']
    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        context = super(PublicationIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        country_filter = request.GET.get('country', None)
        search_filter = request.GET.get('q', None)

        if topic_filter:
            stories = PublicationPage.objects.live().filter(topics__slug=topic_filter)
        else:
            stories = PublicationPage.objects.live()

        if country_filter:
            stories = stories.filter(countries__slug=country_filter)

        if search_filter:
            pass

        paginator = Paginator(stories, MAX_PAGE_SIZE)
        try:
            context['stories'] = paginator.page(page)
        except PageNotAnInteger:
            context['stories'] = paginator.page(1)
        except EmptyPage:
            context['stories'] = paginator.page(paginator.num_pages)

        pubs_content_type = ContentType.objects.get_for_model(PublicationPage)
        context['topics'] = Tag.objects.filter(
            publications_publicationtopic_items__content_object__content_type=pubs_content_type
        ).distinct()
        context['selected_topic'] = topic_filter
        context['countries'] = PublicationCountry.objects.all()
        context['selected_country'] = country_filter
        context['paginator_range'] = get_paginator_range(paginator, context['stories'])

        return context

    class Meta():
        verbose_name = 'Publication Index Page'


class PublicationPage(HeroMixin, FlexibleContentMixin, Page):
    topics = ClusterTaggableManager(through=PublicationTopic, blank=True)
    countries = models.ForeignKey(
        PublicationCountry, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('topics'),
        FieldPanel('countries'),
        ContentPanel(),
    ]

    class Meta():
        verbose_name = 'Publication Page'
