from django.utils.timezone import now
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
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    StructBlock,
    URLBlock
)
from wagtail.images.blocks import ImageChooserBlock


from taggit.models import Tag, TaggedItemBase

from di_website.common.base import call_to_action_panel, hero_panels, get_paginator_range, get_related_pages
from di_website.common.mixins import OtherPageMixin, HeroMixin, TypesetBodyFootnoteMixin, CallToActionMixin
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS
from di_website.ourteam.models import TeamMemberPage


class BlogTopic(TaggedItemBase):
    content_object = ParentalKey('blog.BlogArticlePage', on_delete=models.CASCADE, related_name='blog_topics')


class BlogIndexPage(HeroMixin, Page):
    subpage_types = ['general.General', 'BlogArticlePage']
    parent_page_types = ['home.HomePage']

    class Meta():
        verbose_name = 'Blog Index Page'

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        if topic_filter:
            articles = BlogArticlePage.objects.live().filter(topics__slug=topic_filter).order_by('-published_date')
        else:
            articles = BlogArticlePage.objects.live().order_by('-published_date')

        if not request.user.is_authenticated:
            articles = articles.public()

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
        ).distinct().order_by('name')
        context['selected_topic'] = topic_filter
        context['paginator_range'] = get_paginator_range(paginator, context['articles'])

        return context

    content_panels = Page.content_panels + [
        hero_panels(),
        InlinePanel('page_notifications', label='Notifications')
    ]


class BlogArticlePage(TypesetBodyFootnoteMixin, HeroMixin, CallToActionMixin, Page):
    topics = ClusterTaggableManager(through=BlogTopic, blank=True)

    internal_author_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The author's page if the author has an internal profile. Photograph, job title, and page link will be drawn from this.",
        verbose_name='Internal Author'
    )
    other_authors = StreamField(
        [
            ('internal_author', PageChooserBlock(
                required=False, target_model='ourteam.TeamMemberPage', icon='user', label='Internal Author')),
            ('external_author', StructBlock([
                ('name', CharBlock(required=False)),
                ('title', CharBlock(required=False)),
                ('photograph', ImageChooserBlock(required=False)),
                ('page', URLBlock(required=False))
            ], icon='user', label='External Author'))
        ],
        blank=True,
        help_text="Additional authors. If order is important, please use this instead of internal author page.",
        verbose_name='Other Authors')

    published_date = models.DateTimeField(
        blank=True,
        default=now,
        help_text='This date will be used for display and ordering',
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            PageChooserPanel('internal_author_page', TeamMemberPage),
            StreamFieldPanel('other_authors')
        ], heading="Author information"),
        call_to_action_panel(),
        FieldPanel('topics'),
        StreamFieldPanel('body'),
        FieldPanel('published_date'),
        InlinePanel('blog_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['general.General']
    parent_page_types = [
        'BlogIndexPage'
    ]

    class Meta():
        verbose_name = 'Blog Article Page'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['related_pages'] = get_related_pages(
            self, self.blog_related_links.all(), BlogArticlePage.objects)

        return context


class BlogPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='blog_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]
