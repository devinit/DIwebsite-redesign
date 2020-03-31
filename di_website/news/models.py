from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    StructBlock,
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page

from taggit.models import Tag, TaggedItemBase

from di_website.common.base import hero_panels, get_paginator_range, get_related_pages
from di_website.common.mixins import OtherPageMixin, HeroMixin, TypesetBodyMixin
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS, RICHTEXT_FEATURES_NO_FOOTNOTES
from di_website.home.models import NewsLetter
from di_website.publications.mixins import PublishedDateMixin
from di_website.publications.utils import PublishedDatePanel


class NewsTopic(TaggedItemBase):
    content_object = ParentalKey('news.NewsStoryPage', on_delete=models.CASCADE, related_name='news_topics')


class NewsIndexPage(HeroMixin, Page):
    intro = RichTextField(blank=True, null=True, help_text="Something about our newsletters", features=RICHTEXT_FEATURES_NO_FOOTNOTES)

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('intro'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['NewsStoryPage', 'general.General']
    parent_page_types = ['whatwedo.WhatWeDoPage']

    class Meta():
        verbose_name = 'News Index Page'

    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            news_stories = NewsStoryPage.objects.live().filter(topics__slug=topic_filter).order_by('-published_date')
        else:
            news_stories = NewsStoryPage.objects.live().order_by('-published_date')

        paginator = Paginator(news_stories, MAX_PAGE_SIZE)
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
        context['newsletter'] = NewsLetter.objects.first()

        return context


class NewsStoryPage(TypesetBodyMixin, PublishedDateMixin, HeroMixin, Page):
    topics = ClusterTaggableManager(through=NewsTopic, blank=True)
    press_release = models.BooleanField(
        default=False, help_text="Should this page appear in the Media Center?")

    content_panels = Page.content_panels + [
        hero_panels(),
        PublishedDatePanel(),
        FieldPanel('press_release'),
        FieldPanel('topics'),
        StreamFieldPanel('body'),
        InlinePanel('news_related_links', label="Related links", max_num=MAX_RELATED_LINKS),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['general.General']
    parent_page_types = [
        'NewsIndexPage'
    ]

    class Meta():
        verbose_name = 'News Story Page'

    def get_context(self, request):
        context = super().get_context(request)

        context['related_pages'] = get_related_pages(
            self.news_related_links.all(), NewsStoryPage.objects)

        return context


class NewsPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='news_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'events.EventPage',
            'news.NewsStoryPage',
            'blog.BlogArticlePage',
            'publications.PublicationPage',
            'publications.ShortPublicationPage',
            'publications.LegacyPublicationPage'
        ])
    ]


class ContactBlock(StructBlock):
    name = CharBlock(required=False)
    telephone = CharBlock(required=False)
    email = CharBlock(required=False)


class PersonBlock(StructBlock):
    person = PageChooserBlock(page_type="ourteam.TeamMemberPage", required=False)

    class Meta:
        template = "blocks/person_block.html"


class MediaCenterPage(TypesetBodyMixin, HeroMixin, Page):
    contact_box = StreamField([
        ('contact', ContactBlock())
    ], null=True, blank=True)
    spokespeople = StreamField([
        ('person', PersonBlock())
    ], null=True, blank=True)

    def get_context(self, request):
        context = super(MediaCenterPage, self).get_context(request)
        page = request.GET.get('page', None)
        news_stories = NewsStoryPage.objects.live().filter(press_release=True).order_by('-published_date')

        paginator = Paginator(news_stories, MAX_PAGE_SIZE)
        try:
            context['stories'] = paginator.page(page)
        except PageNotAnInteger:
            context['stories'] = paginator.page(1)
        except EmptyPage:
            context['stories'] = paginator.page(paginator.num_pages)

        context['paginator_range'] = get_paginator_range(paginator, context['stories'])

        return context

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('contact_box'),
        StreamFieldPanel('body'),
        StreamFieldPanel('spokespeople'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    class Meta():
        verbose_name = 'Media Center Page'

    subpage_types = ['general.General']
    parent_page_types = [
        'home.HomePage'
    ]
