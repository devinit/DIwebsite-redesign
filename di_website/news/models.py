from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Orderable

from taggit.models import Tag, TaggedItemBase

from di_website.common.base import StandardPage, get_paginator_range
from di_website.common.blocks import BaseStreamBlock


class NewsTopic(TaggedItemBase):
    content_object = ParentalKey('news.NewsStoryPage', on_delete=models.CASCADE, related_name='news_topics')


class NewsIndexPage(StandardPage):
    intro = RichTextField(blank=True, null=True, help_text="Something about our newsletters")

    content_panels = StandardPage.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ['NewsStoryPage']
    parent_page_types = ['home.HomePage']

    class Meta():
        verbose_name = 'News Index Page'

    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            news_stories = NewsStoryPage.objects.live().filter(topics__slug=topic_filter)
        else:
            news_stories = NewsStoryPage.objects.live()

        paginator = Paginator(news_stories, 10)
        try:
            context['stories'] = paginator.page(page)
        except PageNotAnInteger:
            context['stories'] = paginator.page(1)
        except EmptyPage:
            context['stories'] = paginator.page(paginator.num_pages)

        news_content_type = ContentType.objects.get_for_model(NewsStoryPage)
        context['topics'] = Tag.objects.filter(
            news_newstopic_items__content_object__content_type=news_content_type
        ).distinct()
        context['selected_topic'] = topic_filter
        context['paginator_range'] = get_paginator_range(paginator, context['stories'])

        return context


class NewsStoryPage(StandardPage):
    topics = ClusterTaggableManager(through=NewsTopic, blank=True)

    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    content_panels = StandardPage.content_panels + [
        FieldPanel('topics'),
        StreamFieldPanel('body'),
        InlinePanel('related_links', label="Related links")
    ]

    parent_page_types = [
        'NewsIndexPage'
    ]

    class Meta():
        verbose_name = 'News Story Page'


class NewsPageRelatedLink(Orderable):
    page = ParentalKey(NewsStoryPage, on_delete=models.CASCADE, related_name='related_links')
    related_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel('related_link', NewsStoryPage)
    ]
