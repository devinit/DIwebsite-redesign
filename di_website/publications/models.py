from num2words import num2words
from itertools import chain

from django import forms
from django.db import models
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from django.utils.text import slugify

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    StructBlock,
    URLBlock
)
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.redirects.models import Redirect
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from di_website.common.base import hero_panels, get_paginator_range
from di_website.common.mixins import HeroMixin
from di_website.common.constants import MAX_PAGE_SIZE
from di_website.downloads.utils import DownloadsPanel, DownloadGroupsPanel
from di_website.ourteam.models import TeamMemberPage

from taggit.models import Tag, TaggedItemBase

from .mixins import FlexibleContentMixin, UniquePageMixin, PageSearchMixin, PublishedDateMixin, UUIDMixin, ReportChildMixin
from .utils import ContentPanel, PublishedDatePanel, WagtailImageField, UUIDPanel, get_first_child_of_type, get_ordered_children_of_type, get_downloads
from .edit_handlers import MultiFieldPanel
from .inlines import *

RED = ''
BLUE = 'body--bluebell'
PINK = 'body--rose'
YELLOW = 'body--sunflower'
ORANGE = 'body--marigold'
PURPLE = 'body--lavendar'
COLOUR_CHOICES = (
    (RED, 'Red'),
    (BLUE, 'Blue'),
    (PINK, 'Pink'),
    (YELLOW, 'Yellow'),
    (ORANGE, 'Orange'),
    (PURPLE, 'Purple'),
)


class PublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.PublicationPage', on_delete=models.CASCADE, related_name='publication_topics')


class LegacyPublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.LegacyPublicationPage', on_delete=models.CASCADE, related_name='legacy_publication_topics')


class ShortPublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.ShortPublicationPage', on_delete=models.CASCADE, related_name='short_publication_topics')


@register_snippet
class PublicationRegion(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)

    panels = [
        FieldPanel('name'),
    ]

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


@register_snippet
class PublicationCountry(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(
        PublicationRegion, related_name="+", on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        help_text="Optional. Will be auto-generated from name if left blank.")

    panels = [
        FieldPanel('name'),
        SnippetChooserPanel('region'),
        FieldPanel('slug'),
    ]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Publication countries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(PublicationCountry, self).save(*args, **kwargs)


@register_snippet
class PublicationType(ClusterableModel):
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
        super(PublicationType, self).save(*args, **kwargs)


class PublicationIndexPage(HeroMixin, Page):

    content_panels = Page.content_panels + [
        hero_panels()
    ]

    subpage_types = ['PublicationPage', 'LegacyPublicationPage']
    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        context = super(PublicationIndexPage, self).get_context(request)
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        country_filter = request.GET.get('country', None)
        search_filter = request.GET.get('q', None)

        if topic_filter:
            stories = PublicationPage.objects.live().filter(topics__slug=topic_filter)
            legacy_pubs = LegacyPublicationPage.objects.live().filter(topics__slug=topic_filter)
            short_pubs = ShortPublicationPage.objects.live().filter(topics__slug=topic_filter)
        else:
            stories = PublicationPage.objects.live()
            legacy_pubs = LegacyPublicationPage.objects.live()
            short_pubs = ShortPublicationPage.objects.live()

        if country_filter:
            stories = stories.filter(countries__slug=country_filter)
            legacy_pubs = legacy_pubs.filter(countries__slug=country_filter)
            short_pubs = short_pubs.filter(countries__slug=country_filter)

        if search_filter:
            stories = stories.search(search_filter)
            legacy_pubs = legacy_pubs.search(search_filter)
            short_pubs = short_pubs.search(search_filter)

        paginator = Paginator(list(chain(stories, legacy_pubs, short_pubs)), MAX_PAGE_SIZE)
        try:
            context['stories'] = paginator.page(page)
        except PageNotAnInteger:
            context['stories'] = paginator.page(1)
        except EmptyPage:
            context['stories'] = paginator.page(paginator.num_pages)

        pubs_content_type = ContentType.objects.get_for_model(PublicationPage)
        leg_pubs_content_type = ContentType.objects.get_for_model(LegacyPublicationPage)
        short_pubs_content_type = ContentType.objects.get_for_model(ShortPublicationPage)
        context['topics'] = Tag.objects.filter(
            Q(publications_publicationtopic_items__content_object__content_type=pubs_content_type) |
            Q(publications_legacypublicationtopic_items__content_object__content_type=leg_pubs_content_type) |
            Q(publications_shortpublicationtopic_items__content_object__content_type=short_pubs_content_type)
        ).distinct()
        context['selected_topic'] = topic_filter
        context['countries'] = PublicationCountry.objects.all()
        context['selected_country'] = country_filter
        context['search_filter'] = search_filter
        context['paginator_range'] = get_paginator_range(paginator, context['stories'])

        return context

    class Meta():
        verbose_name = 'Publication Index Page'


class PublicationPage(HeroMixin, PublishedDateMixin, UUIDMixin, Page):

    class Meta:
        verbose_name = 'Publication Page'

    parent_page_types = ['PublicationIndexPage']
    subpage_types = [
        'PublicationSummaryPage',
        'PublicationChapterPage',
        'PublicationAppendixPage',
    ]

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=BLUE)

    authors = StreamField([
        ('internal_author', PageChooserBlock(required=False, target_model='ourteam.TeamMemberPage')),
        ('external_author', StructBlock([
            ('name', CharBlock(required=False)),
            ('title', CharBlock(required=False)),
            ('photograph', ImageChooserBlock(required=False)),
            ('page', URLBlock(required=False))
        ]))
    ], blank=True)

    publication_type = models.ForeignKey(
        PublicationType, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    topics = ClusterTaggableManager(through=PublicationTopic, blank=True, verbose_name="Topics")
    countries = models.ForeignKey(
        PublicationCountry, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        StreamFieldPanel('authors'),
        SnippetChooserPanel('publication_type'),
        FieldPanel('topics'),
        SnippetChooserPanel('countries'),
        PublishedDatePanel(),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this report.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this report.',
            max_num=1,
        ),
        UUIDPanel(),
    ]

    @cached_property
    def publication_downloads_title(self):
        return 'Downloads'

    @cached_property
    def publication_downloads_list(self):
        return get_downloads(self)

    @cached_property
    def data_downloads_title(self):
        return 'Data downloads'

    @cached_property
    def data_downloads_list(self):
        return get_downloads(self, with_parent=False, data=True)

    @cached_property
    def page_publication_downloads(self):
        return self.publication_downloads.all()

    @cached_property
    def page_data_downloads(self):
        return self.data_downloads.all()

    @cached_property
    def summary(self):
        return get_first_child_of_type(self, PublicationSummaryPage)

    @cached_property
    def chapters(self):
        return get_ordered_children_of_type(self, PublicationChapterPage, 'publicationchapterpage__chapter_number')

    @cached_property
    def appendices(self):
        return get_ordered_children_of_type(self, PublicationAppendixPage, 'publicationappendixpage__appendix_number')

    @cached_property
    def listing(self):
        children = [self.summary]
        children += list(self.chapters)
        return filter(None, children)

    @cached_property
    def meta_and_appendices(self):
        children = list()
        children += list(self.appendices)
        return filter(None, children)

    def save(self, *args, **kwargs):
        super(PublicationPage, self).save(*args, **kwargs)

        old_path = '/%s' % self.slug
        redirect = Redirect.objects.filter(old_path=old_path).first()
        if not redirect:
            Redirect(old_path=old_path, redirect_page=self).save()


class PublicationSummaryPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UniquePageMixin, UUIDMixin, Page):

    class Meta:
        verbose_name = 'Publication summary'
        verbose_name_plural = 'Publication summaries'

    parent_page_types = ['PublicationPage']
    subpage_types = []

    template = 'publications/publication_chapter_page.html'

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=BLUE)

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        ContentPanel(),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this summary.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this summary.',
            max_num=1,
        ),
    ]

    @cached_property
    def label(self):
        return 'The summary'


class PublicationChapterPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, Page):

    class Meta:
        verbose_name = 'Publication chapter'

    parent_page_types = ['PublicationPage']
    subpage_types = []

    chapter_number = models.PositiveIntegerField(
        choices=[(i, num2words(i).title()) for i in range(1, 21)]
    )
    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=BLUE)

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        MultiFieldPanel(
            [
                FieldPanel('chapter_number', widget=forms.Select),
            ],
            heading='Chapter number',
            description='Chapter number: this should be unique for each chapter of a report.'
        ),
        ContentPanel(),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this chapter.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this chapter.',
            max_num=1,
        ),
    ]

    @cached_property
    def chapter_word(self):
        return num2words(self.chapter_number)

    @cached_property
    def label(self):
        return 'chapter %s' % self.chapter_word

    @cached_property
    def label_num(self):
        return 'chapter %s' % str(self.chapter_number).zfill(2)

    @cached_property
    def sections(self):
        sections = []
        for block in self.content:
            if block.block_type == 'section_heading':
                sections.append(block)
        return sections


class PublicationAppendixPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, Page):

    class Meta:
        verbose_name = 'Publication appendix'
        verbose_name_plural = 'Publication appendices'

    parent_page_types = ['PublicationPage']
    subpage_types = []

    template = 'publications/publication_chapter_page.html'

    appendix_number = models.PositiveIntegerField(
        choices=[(i, num2words(i).title()) for i in range(1, 21)]
    )
    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=BLUE)

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        MultiFieldPanel(
            [
                FieldPanel('appendix_number', widget=forms.Select),
            ],
            heading='Appendix number',
            description='Appendix number: this should be unique for each appendix of a report.'
        ),
        ContentPanel(),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this appendix page.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this appendix page.',
            max_num=1,
        ),
    ]

    @cached_property
    def appendix_word(self):
        return num2words(self.appendix_number)

    @cached_property
    def label(self):
        return 'appendix %s' % self.appendix_word

    @cached_property
    def label_num(self):
        return 'appendix %s' % str(self.appendix_number).zfill(2)


class LegacyPublicationPage(HeroMixin, PublishedDateMixin, PageSearchMixin, Page):

    class Meta:
        verbose_name = 'Legacy publication'

    parent_page_types = ['PublicationIndexPage']
    subpage_types = []

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=BLUE)
    authors = StreamField([
        ('internal_author', PageChooserBlock(required=False, target_model='ourteam.TeamMemberPage')),
        ('external_author', StructBlock([
            ('name', CharBlock(required=False)),
            ('title', CharBlock(required=False)),
            ('photograph', ImageChooserBlock(required=False)),
            ('page', URLBlock(required=False))
        ]))
    ], blank=True)

    publication_type = models.ForeignKey(
        PublicationType, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    topics = ClusterTaggableManager(through=LegacyPublicationTopic, blank=True, verbose_name="Topics")
    countries = models.ForeignKey(
        PublicationCountry, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)

    content = RichTextField(
        verbose_name='Summary',
        help_text='Short summary for the legacy report',
    )
    summary_image = WagtailImageField(
        required=False,
        help_text='Optimal minimum size 800x400px',
    )

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        StreamFieldPanel('authors'),
        SnippetChooserPanel('publication_type'),
        FieldPanel('topics'),
        SnippetChooserPanel('countries'),
        PublishedDatePanel(),
        DownloadsPanel(
            heading='Reports',
            description='Report downloads for this legacy report.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this legacy report.',
            max_num=1,
        ),
        MultiFieldPanel(
            [
                FieldPanel('content'),
                ImageChooserPanel('summary_image'),
            ],
            heading='Summary',
            description='Summary for the legacy publication.'
        ),
        DownloadGroupsPanel(),
    ]

    @cached_property
    def page_publication_downloads(self):
        return self.publication_downloads.all()

    @cached_property
    def page_data_downloads(self):
        return self.data_downloads.all()

    @cached_property
    def groups(self):
        return self.download_groups.all()


class ShortPublicationPage(HeroMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, Page):

    class Meta:
        verbose_name = 'Short publication'

    parent_page_types = ['PublicationIndexPage']
    subpage_types = []

    template = 'publications/publication_chapter_page.html'

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=BLUE)
    publication_type = models.ForeignKey(
        PublicationType, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    topics = ClusterTaggableManager(through=ShortPublicationTopic, blank=True, verbose_name="Topics")
    countries = models.ForeignKey(
        PublicationCountry, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        SnippetChooserPanel('publication_type'),
        FieldPanel('topics'),
        SnippetChooserPanel('countries'),
        ContentPanel(),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this chapter.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this chapter.',
            max_num=1,
        ),
    ]
