from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel,
    MultiFieldPanel, PageChooserPanel,
    StreamFieldPanel)
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from taggit.models import Tag, TaggedItemBase

from di_website.common.base import hero_panels, get_paginator_range
from di_website.common.mixins import BaseStreamBodyMixin, OtherPageMixin, HeroMixin
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS
from di_website.ourteam.models import TeamMemberPage


class BlogTopic(TaggedItemBase):
    content_object = ParentalKey('blog.BlogArticlePage', on_delete=models.CASCADE, related_name='blog_topics')


class BlogIndexPage(HeroMixin, Page):
    subpage_types = ['BlogArticlePage']

    class Meta():
        verbose_name = 'Blog Index Page'

    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            articles = BlogArticlePage.objects.live().filter(topics__slug=topic_filter)
        else:
            articles = BlogArticlePage.objects.live()

        paginator = Paginator(articles, MAX_PAGE_SIZE)
        try:
            context['articles'] = paginator.page(page)
        except PageNotAnInteger:
            context['articles'] = paginator.page(1)
        except EmptyPage:
            context['articles'] = paginator.page(paginator.num_pages)

        blog_content_type = ContentType.objects.get_for_model(BlogArticlePage)
        context['topics'] = Tag.objects.filter(
            blog_blogtopic_items__content_object__content_type=blog_content_type
        ).distinct()
        context['selected_topic'] = topic_filter
        context['paginator_range'] = get_paginator_range(paginator, context['articles'])

        return context

    content_panels = Page.content_panels + [hero_panels()]


class BlogArticlePage(BaseStreamBodyMixin, HeroMixin, Page):
    topics = ClusterTaggableManager(through=BlogTopic, blank=True)

    internal_author_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The author's page if the author has an internal profile. Photograph, job title, and page link will be drawn from this."
    )
    external_author_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Only fill out for guest authors."
    )
    external_author_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Only fill out for guest authors."
    )
    external_author_photograph = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Only fill out for guest authors."
    )
    external_author_page = models.URLField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="Only fill out for guest authors."
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            PageChooserPanel('internal_author_page', TeamMemberPage),
            FieldPanel('external_author_name'),
            FieldPanel('external_author_title'),
            ImageChooserPanel('external_author_photograph'),
            FieldPanel('external_author_page'),
        ], heading="Author information"),
        FieldPanel('topics'),
        StreamFieldPanel('body'),
        InlinePanel('blog_related_links', label="Related links", max_num=MAX_RELATED_LINKS)
    ]

    parent_page_types = [
        'BlogIndexPage'
    ]

    class Meta():
        verbose_name = 'Blog Article Page'

    def get_related_pages(self):
        related_links = self.blog_related_links.all()
        related_links_count = len(related_links)

        if related_links_count < MAX_RELATED_LINKS:
            difference = MAX_RELATED_LINKS - related_links_count
            related_pages = [link.other_page for link in related_links]
            id_list = [page.id for page in related_pages]
            blog_pages = BlogArticlePage.objects.live()
            placeholder_pages = blog_pages.exclude(id__in=id_list).exclude(id=self.id)[:difference]
            related_links = list(related_pages) + list(placeholder_pages)

        return related_links

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['related_pages'] = self.get_related_pages()

        return context


class BlogPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='blog_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'events.EventPage',
            'blog.BlogArticlePage',
            'news.NewsStoryPage'
        ])
    ]
