from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page

from taggit.models import Tag, TaggedItemBase

from di_website.common.base import hero_panels, get_paginator_range
from di_website.common.mixins import BaseStreamBodyMixin, OtherPageMixin, HeroMixin
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS


class NewsTopic(TaggedItemBase):
    content_object = ParentalKey('news.NewsStoryPage', on_delete=models.CASCADE, related_name='news_topics')


class NewsIndexPage(HeroMixin, Page):
    intro = RichTextField(blank=True, null=True, help_text="Something about our newsletters")

    content_panels = Page.content_panels + [
        hero_panels(),
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

        return context


class NewsStoryPage(BaseStreamBodyMixin, HeroMixin, Page):
    topics = ClusterTaggableManager(through=NewsTopic, blank=True)
    press_release = models.BooleanField(default=False, help_text="Should this page appear in the Media Center?")

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('press_release'),
        FieldPanel('topics'),
        StreamFieldPanel('body'),
        InlinePanel('news_related_links', label="Related links", max_num=MAX_RELATED_LINKS)
    ]

    parent_page_types = [
        'NewsIndexPage'
    ]

    class Meta():
        verbose_name = 'News Story Page'

    def get_context(self, request):
        context = super().get_context(request)

        related_links = self.news_related_links.all()
        related_links_count = len(related_links)

        if related_links_count < MAX_RELATED_LINKS:
            difference = MAX_RELATED_LINKS - related_links_count
            news_pages = [link.page for link in related_links]
            id_list = [page.id for page in news_pages]
            news_objects = NewsStoryPage.objects.live()
            related_links = news_objects.filter(id__in=id_list) | news_objects.exclude(id__in=id_list)[:difference]

        context['related_pages'] = related_links

        return context


class NewsPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='news_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', ['news.NewsStoryPage', 'blog.BlogArticlePage'])
    ]


class ContactBlock(StructBlock):
    name = CharBlock(required=False)
    telephone = CharBlock(required=False)
    email = CharBlock(required=False)


class PersonBlock(StructBlock):
    person = PageChooserBlock(page_type="ourteam.TeamMemberPage", required=False)

    class Meta:
        template = "blocks/person_block.html"


class MediaCenterPage(BaseStreamBodyMixin, HeroMixin, Page):
    contact_box = StreamField([
        ('contact', ContactBlock())
    ], null=True, blank=True)
    spokespeople = StreamField([
        ('spokesperson', PersonBlock())
    ], null=True, blank=True)

    def get_context(self, request):
        context = super(MediaCenterPage, self).get_context(request)
        page = request.GET.get('page', None)
        news_stories = NewsStoryPage.objects.live().filter(press_release=True)

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
    ]
