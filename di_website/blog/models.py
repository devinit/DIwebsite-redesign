from django.db import models
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import (
    PageChooserPanel,
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from di_website.common.base import StandardPage, get_paginator_range
from di_website.common.blocks import BaseStreamBlock


@register_snippet
class BlogTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, help_text="Optional. Will be auto-generated from name if left blank.")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(BlogTopic, self).save(*args, **kwargs)


class BlogIndexPage(StandardPage):
    subpage_types = ['BlogArticlePage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            articles = BlogArticlePage.objects.live().filter(topic__slug=topic_filter)
        else:
            articles = BlogArticlePage.objects.live()

        paginator = Paginator(articles, 10)
        try:
            context['articles'] = paginator.page(page)
        except PageNotAnInteger:
            context['articles'] = paginator.page(1)
        except EmptyPage:
            context['articles'] = paginator.page(paginator.num_pages)
        context['topics'] = BlogTopic.objects.all()
        context['selected_topic'] = topic_filter
        context['paginator_range'] = get_paginator_range(paginator)

        return context


class BlogArticlePage(StandardPage):
    topic = models.ForeignKey(
        BlogTopic,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    internal_author_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The author's page if the author has an internal profile. Photograph, job title, and page link will be drawn from this."
    )
    external_author_name = models.CharField(max_length=255, null=True, blank=True, help_text="Only fill out for guest authors.")
    external_author_title = models.CharField(max_length=255, null=True, blank=True, help_text="Only fill out for guest authors.")
    external_author_photograph = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Only fill out for guest authors."
    )
    external_author_page = models.URLField(max_length=1000, null=True, blank=True, help_text="Only fill out for guest authors.")
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        blank=True
    )

    content_panels = StandardPage.content_panels + [
        MultiFieldPanel([
            PageChooserPanel('internal_author_page'),
            FieldPanel('external_author_name'),
            FieldPanel('external_author_title'),
            ImageChooserPanel('external_author_photograph'),
            FieldPanel('external_author_page'),
        ], heading="Author information"),
        MultiFieldPanel([
            SnippetChooserPanel('topic'),
            StreamFieldPanel('body'),
        ], heading="Content")
    ]

    parent_page_types = [
        'BlogIndexPage'
    ]
