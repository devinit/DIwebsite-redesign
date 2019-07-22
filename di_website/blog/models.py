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
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

from taggit.models import Tag, TaggedItemBase

from di_website.common.base import StandardPage, get_paginator_range
from di_website.common.blocks import BaseStreamBlock
from di_website.ourteam.models import TeamMemberPage


class BlogTopic(TaggedItemBase):
    content_object = ParentalKey('blog.BlogArticlePage', on_delete=models.CASCADE, related_name='blog_topics')


class BlogIndexPage(StandardPage):
    subpage_types = ['BlogArticlePage']

    class Meta():
        verbose_name = 'Blog Index Page'

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            articles = BlogArticlePage.objects.live().filter(topics__slug=topic_filter)
        else:
            articles = BlogArticlePage.objects.live()

        paginator = Paginator(articles, 10)
        try:
            context['articles'] = paginator.page(page)
        except PageNotAnInteger:
            context['articles'] = paginator.page(1)
        except EmptyPage:
            context['articles'] = paginator.page(paginator.num_pages)

        blog_content_type = ContentType.objects.get_for_model(BlogArticlePage)
        context['topics'] = Tag.objects.filter(
            blog_blogtopic_items__content_object__content_type=blog_content_type
        )
        context['selected_topic'] = topic_filter
        context['paginator_range'] = get_paginator_range(paginator, context['articles'])

        return context


class BlogArticlePage(StandardPage):
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
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    content_panels = StandardPage.content_panels + [
        MultiFieldPanel([
            PageChooserPanel('internal_author_page', TeamMemberPage),
            FieldPanel('external_author_name'),
            FieldPanel('external_author_title'),
            ImageChooserPanel('external_author_photograph'),
            FieldPanel('external_author_page'),
        ], heading="Author information"),
        FieldPanel('topics'),
        StreamFieldPanel('body'),
        InlinePanel('related_links', label="Related links")
    ]

    parent_page_types = [
        'BlogIndexPage'
    ]


class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogArticlePage, on_delete=models.CASCADE, related_name='related_links')
    related_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel('related_link', BlogArticlePage)
    ]
