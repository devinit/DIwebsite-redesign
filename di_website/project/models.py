from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    InlinePanel,
    PageChooserPanel,
    MultiFieldPanel,
    FieldPanel
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin, OtherPageMixin
from di_website.common.blocks import BaseStreamBlock
from di_website.common.constants import MAX_RELATED_LINKS


class ProjectPage(BaseStreamBodyMixin, HeroMixin, Page):
    other_pages_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Section Title'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('project_related_links',
                        label="Related links", max_num=MAX_RELATED_LINKS)
        ], heading='Other Pages')
    ]


class ProjectPageRelatedLink(OtherPageMixin):
    page = ParentalKey(
        Page, related_name='project_related_links', on_delete=models.CASCADE)
    panels = [
        PageChooserPanel('other_page')
    ]

# class FocusAreasPage(StandardPage):
#     subpage_types = ['ProjectPage']

#     class Meta():
#         verbose_name = 'Focus Areas Page'

#     def get_context(self, request):
#         context = super(FocusAreasPage, self).get_context(request)
#         page = request.GET.get('page', None)

        # articles = BlogArticlePage.objects.live()



        # # paginator = Paginator(articles, 10)
        # # try:
        # #     context['articles'] = paginator.page(page)
        # # except PageNotAnInteger:
        # #     context['articles'] = paginator.page(1)
        # # except EmptyPage:
        # #     context['articles'] = paginator.page(paginator.num_pages)

        # # blog_content_type = ContentType.objects.get_for_model(BlogArticlePage)
        # # context['topics'] = Tag.objects.filter(
        # #     blog_blogtopic_items__content_object__content_type=blog_content_type
        # # ).distinct()
        # # context['selected_topic'] = topic_filter
        # # context['paginator_range'] = get_paginator_range(paginator, context['articles'])

        # # return context
