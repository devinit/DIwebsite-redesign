from num2words import num2words
from itertools import chain
import operator
from functools import reduce

from django import forms
from django.db import models
from django.db.models import Q, FloatField, Value
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from django.utils.text import slugify

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core import hooks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    StructBlock,
    URLBlock
)
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.redirects.models import Redirect
from wagtail.contrib.search_promotions.templatetags.wagtailsearchpromotions_tags import \
    get_search_promotions
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search.models import Query
from wagtail.embeds.blocks import EmbedBlock
from wagtailmedia.edit_handlers import MediaChooserPanel

from di_website.common.base import hero_panels, get_paginator_range, get_related_pages
from di_website.common.mixins import HeroMixin, OtherPageMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS, RICHTEXT_FEATURES
from di_website.downloads.utils import DownloadsPanel

from taggit.models import Tag, TaggedItemBase
from .mixins import (
    FlexibleContentMixin, UniqueForParentPageMixin, PageSearchMixin, LegacyPageSearchMixin, ParentPageSearchMixin,
    PublishedDateMixin, UUIDMixin, ReportChildMixin, FilteredDatasetMixin)
from .utils import (
    ContentPanel, PublishedDatePanel, WagtailImageField,
    UUIDPanel, get_first_child_of_type, get_ordered_children_of_type, get_downloads)
from .edit_handlers import MultiFieldPanel
from .inlines import *


RED = 'poppy'
BLUE = 'bluebell'
PINK = 'rose'
YELLOW = 'sunflower'
ORANGE = 'marigold'
PURPLE = 'lavendar'
GREEN = 'leaf'
COLOUR_CHOICES = (
    (RED, 'Red'),
    (BLUE, 'Blue'),
    (PINK, 'Pink'),
    (YELLOW, 'Yellow'),
    (ORANGE, 'Orange'),
    (PURPLE, 'Purple'),
    (GREEN, 'Green')
)


class PublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.PublicationPage', on_delete=models.CASCADE, related_name='publication_topics')


class LegacyPublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.LegacyPublicationPage', on_delete=models.CASCADE, related_name='legacy_publication_topics')


class ShortPublicationTopic(TaggedItemBase):
    content_object = ParentalKey('publications.ShortPublicationPage', on_delete=models.CASCADE, related_name='short_publication_topics')


@hooks.register('construct_media_chooser_queryset')
def show_my_uploaded_media_only(media, request):
    # Only show uploaded audio files
    media = media.filter(type='audio')

    return media


@register_snippet
class Region(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)

    panels = [
        FieldPanel('name'),
    ]

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


@register_snippet
class Country(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(
        Region, related_name="+", on_delete=models.CASCADE)
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
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)


class PageCountry(Orderable):
    page = ParentalKey(
        Page, related_name='page_countries', on_delete=models.CASCADE
    )

    country = models.ForeignKey(
        Country, related_name="+", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name


@register_snippet
class ResourceCategory(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)

    panels = [
        FieldPanel('name'),
    ]

    class Meta:
        ordering = ["name"]
        verbose_name = 'Resource Category'
        verbose_name_plural = 'Resource Categories'

    def __str__(self):
        return self.name


@register_snippet
class PublicationType(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)
    resource_category = models.ForeignKey(
        ResourceCategory, related_name="+", on_delete=models.CASCADE, null=True, blank=False)
    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        help_text="Optional. Will be auto-generated from name if left blank.")

    panels = [
        FieldPanel('name'),
        SnippetChooserPanel('resource_category'),
        FieldPanel('slug'),
    ]

    class Meta:
        ordering = ["name"]
        verbose_name = 'Resource Type'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(PublicationType, self).save(*args, **kwargs)


class PublicationIndexPage(HeroMixin, Page):

    content_panels = Page.content_panels + [
        hero_panels(),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['PublicationPage', 'LegacyPublicationPage', 'ShortPublicationPage', 'general.General', 'AudioVisualMedia']
    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        context = super(PublicationIndexPage, self).get_context(request)
        sort_options = [
            ('date_desc', 'date descending'),
            ('date_asc', 'date ascending'),
            ('score', 'relevance')
        ]
        sort_ids = [sort_opt[0] for sort_opt in sort_options]
        page = request.GET.get('page', None)
        topic_filter = request.GET.get('topic', None)
        country_filter = request.GET.get('country', None)
        types_filter = request.GET.get('types', None)
        search_filter = request.GET.get('q', None)
        selected_sort = request.GET.get('sort', 'date_desc')
        if selected_sort not in sort_ids:
            selected_sort = 'date_desc'
        if not search_filter and selected_sort == "score":
            selected_sort = 'date_desc'

        if topic_filter:
            stories = PublicationPage.objects.live().filter(topics__slug=topic_filter)
            legacy_pubs = LegacyPublicationPage.objects.live().filter(topics__slug=topic_filter)
            short_pubs = ShortPublicationPage.objects.live().filter(topics__slug=topic_filter)
            audio_visual_media = AudioVisualMedia.objects.live().filter(topics__slug=topic_filter)
        else:
            stories = PublicationPage.objects.live()
            legacy_pubs = LegacyPublicationPage.objects.live()
            short_pubs = ShortPublicationPage.objects.live()
            audio_visual_media = AudioVisualMedia.objects.live()

        if country_filter:
            stories = stories.filter(page_countries__country__slug=country_filter)
            legacy_pubs = legacy_pubs.filter(page_countries__country__slug=country_filter)
            short_pubs = short_pubs.filter(page_countries__country__slug=country_filter)

        if types_filter:
            stories = stories.filter(publication_type__slug=types_filter)
            legacy_pubs = legacy_pubs.filter(publication_type__slug=types_filter)
            short_pubs = short_pubs.filter(publication_type__slug=types_filter)
            audio_visual_media = audio_visual_media.filter(publication_type__slug=types_filter)

        if search_filter:
            query = Query.get(search_filter)
            query.add_hit()
            if stories:
                child_count = reduce(operator.add, [len(pub.get_children()) for pub in stories])
                if child_count:
                    pub_children = reduce(operator.or_, [pub.get_children() for pub in stories]).live().specific().search(search_filter).annotate_score("_child_score")
                    if pub_children:
                        matching_parents = reduce(operator.or_, [stories.parent_of(child).annotate(_score=Value(child._child_score, output_field=FloatField())) for child in pub_children])
                        stories = list(chain(stories.search(search_filter).annotate_score("_score"), matching_parents))
                    else:
                        stories = stories.search(search_filter).annotate_score("_score")
                else:
                    stories = stories.search(search_filter).annotate_score("_score")
            legacy_pubs = legacy_pubs.search(search_filter).annotate_score("_score")
            short_pubs = short_pubs.search(search_filter).annotate_score("_score")
            audio_visual_media = audio_visual_media.search(search_filter).annotate_score('_score')

        story_list = list(chain(stories, legacy_pubs, short_pubs, audio_visual_media))
        elasticsearch_is_active = True
        for story in story_list:
            if hasattr(story, "_score"):
                if story._score is None:
                    elasticsearch_is_active = False
        if selected_sort == "score" and elasticsearch_is_active:
            story_list.sort(key=lambda x: x._score, reverse=True)
        elif selected_sort == "date_asc":
            story_list.sort(key=lambda x: x.published_date, reverse=False)
        else:
            story_list.sort(key=lambda x: x.published_date, reverse=True)

        promos = get_search_promotions(search_filter)
        promo_pages = [promo.page.specific for promo in promos if promo.page.live and isinstance(promo.page.specific, (PublicationPage, ShortPublicationPage, LegacyPublicationPage))]
        if promo_pages:
            story_list = [story for story in story_list if story not in promo_pages]
            story_list = list(chain(promo_pages, story_list))

        paginator = Paginator(story_list, MAX_PAGE_SIZE)
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
        ).distinct().order_by('name')
        context['resource_types'] = PublicationType.objects.all().order_by('resource_category', 'name')
        context['selected_type'] = types_filter
        context['selected_topic'] = topic_filter
        context['countries'] = Country.objects.all().order_by('region', 'name')
        context['selected_country'] = country_filter
        context['search_filter'] = search_filter
        context['selected_sort'] = selected_sort
        context['sort_options'] = sort_options
        context['is_filtered'] = search_filter or topic_filter or country_filter
        context['paginator_range'] = get_paginator_range(paginator, context['stories'])

        return context

    class Meta():
        verbose_name = 'Resources Index Page'


class PublicationPage(HeroMixin, PublishedDateMixin, ParentPageSearchMixin, UUIDMixin, FilteredDatasetMixin, Page):

    class Meta:
        verbose_name = 'Publication Page'

    parent_page_types = ['PublicationIndexPage', 'general.General']
    subpage_types = [
        'PublicationSummaryPage',
        'PublicationChapterPage',
        'PublicationAppendixPage',
    ]

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=RED)

    authors = StreamField([
        ('internal_author', PageChooserBlock(
            required=False,
            target_model='ourteam.TeamMemberPage',
            icon='fa-user'
        )),
        ('external_author', StructBlock([
            ('name', CharBlock(required=False)),
            ('title', CharBlock(required=False)),
            ('photograph', ImageChooserBlock(required=False)),
            ('page', URLBlock(required=False))
        ], icon='fa-user'))
    ], blank=True)

    publication_type = models.ForeignKey(
        PublicationType, related_name="+", null=True, blank=False, on_delete=models.SET_NULL, verbose_name="Resource Type")
    topics = ClusterTaggableManager(through=PublicationTopic, blank=True, verbose_name="Topics")

    download_report_cover = WagtailImageField()
    download_report_title = models.CharField(max_length=255, null=True, blank=True, default="Download this report")
    download_report_body = models.TextField(null=True, blank=True)
    download_report_button_text = models.CharField(max_length=255, null=True, blank=True, default="Download now")
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        StreamFieldPanel('authors'),
        SnippetChooserPanel('publication_type'),
        FieldPanel('topics'),
        InlinePanel('publication_datasets', label='Datasets'),
        InlinePanel('page_countries', label="Countries"),
        PublishedDatePanel(),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this report.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this report.'
        ),
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        UUIDPanel(),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def publication_downloads_title(self):
        return 'Publication downloads'

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
        return list(filter(None, children))

    @cached_property
    def meta_and_appendices(self):
        children = list()
        children += list(self.appendices)
        return list(filter(None, children))

    @cached_property
    def listing_and_appendicies(self):
        return self.listing + self.meta_and_appendices

    @cached_property
    def chapter_max(self):
        try:
            return max([chapter.chapter_number for chapter in self.chapters])
        except ValueError:
            return 0

    def save(self, *args, **kwargs):
        super(PublicationPage, self).save(*args, **kwargs)

        old_path = '/%s' % self.slug
        redirect = Redirect.objects.filter(old_path=old_path).first()
        if not redirect:
            Redirect(old_path=old_path, redirect_page=self).save()


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['related_pages'] = get_related_pages(
            self.publication_related_links.all(), PublicationPage.objects)

        return context;


class PublicationSummaryPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UniqueForParentPageMixin, UUIDMixin, FilteredDatasetMixin, Page):

    class Meta:
        verbose_name = 'Publication Summary'
        verbose_name_plural = 'Publication Summaries'

    parent_page_types = ['PublicationPage']
    subpage_types = []

    template = 'publications/publication_chapter_page.html'

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=RED)

    download_report_cover = WagtailImageField()
    download_report_title = models.CharField(max_length=255, null=True, blank=True, default="Download this report")
    download_report_body = models.TextField(null=True, blank=True)
    download_report_button_text = models.CharField(max_length=255, null=True, blank=True, default="Download now")
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        ContentPanel(),
        InlinePanel('publication_datasets', label='Datasets'),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this summary.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this summary.'
        ),
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def label_type(self):
        return 'summary'

    @cached_property
    def label(self):
        return 'the executive summary'

    @cached_property
    def publication_downloads_title(self):
        return 'Publication downloads'

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
    def sections(self):
        sections = []
        for block in self.content:
            if block.block_type == 'section_heading':
                sections.append(block)
        return sections


class PublicationChapterPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, FilteredDatasetMixin, Page):

    class Meta:
        verbose_name = 'Publication Chapter'

    parent_page_types = ['PublicationPage']
    subpage_types = []

    chapter_number = models.PositiveIntegerField(
        choices=[(i, num2words(i).title()) for i in range(1, 21)]
    )
    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=RED)

    download_report_cover = WagtailImageField()
    download_report_title = models.CharField(max_length=255, null=True, blank=True, default="Download this report")
    download_report_body = models.TextField(null=True, blank=True)
    download_report_button_text = models.CharField(max_length=255, null=True, blank=True, default="Download now")
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

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
        InlinePanel('publication_datasets', label='Datasets'),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this chapter.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this chapter.'
        ),
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def chapter_word(self):
        return num2words(self.chapter_number)

    @cached_property
    def label_type(self):
        return 'chapter'

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

    @cached_property
    def publication_downloads_title(self):
        return 'Publication downloads'

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


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['related_pages'] = get_related_pages(
            self.publication_related_links.all(), PublicationChapterPage.objects)

        return context;


class PublicationAppendixPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, FilteredDatasetMixin, Page):

    class Meta:
        verbose_name = 'Publication Appendix'
        verbose_name_plural = 'Publication Appendices'

    parent_page_types = ['PublicationPage']
    subpage_types = []

    template = 'publications/publication_chapter_page.html'

    appendix_number = models.PositiveIntegerField(
        choices=[(i, num2words(i).title()) for i in range(1, 21)]
    )
    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=RED)

    download_report_cover = WagtailImageField()
    download_report_title = models.CharField(max_length=255, null=True, blank=True, default="Download this report")
    download_report_body = models.TextField(null=True, blank=True)
    download_report_button_text = models.CharField(max_length=255, null=True, blank=True, default="Download now")
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

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
        InlinePanel('publication_datasets', label='Datasets'),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this appendix page.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this appendix page.'
        ),
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def appendix_word(self):
        return num2words(self.appendix_number)

    @cached_property
    def label_type(self):
        return 'appendix'

    @cached_property
    def label(self):
        return 'appendix %s' % self.appendix_word

    @cached_property
    def label_num(self):
        return 'appendix %s' % str(self.appendix_number).zfill(2)

    @cached_property
    def publication_downloads_title(self):
        return 'Publication downloads'

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
    def sections(self):
        sections = []
        for block in self.content:
            if block.block_type == 'section_heading':
                sections.append(block)
        return sections


class LegacyPublicationPage(HeroMixin, PublishedDateMixin, LegacyPageSearchMixin, FilteredDatasetMixin, Page):

    class Meta:
        verbose_name = 'Legacy Publication'

    parent_page_types = ['PublicationIndexPage']
    subpage_types = []

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=RED)
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
        PublicationType, related_name="+", null=True, blank=False, on_delete=models.SET_NULL, verbose_name="Resource Type")
    topics = ClusterTaggableManager(through=LegacyPublicationTopic, blank=True, verbose_name="Topics")

    raw_content = models.TextField(null=True, blank=True)
    content = RichTextField(
        help_text='Content for the legacy report',
        null=True, blank=True,
        features=RICHTEXT_FEATURES
    )
    summary_image = WagtailImageField(
        required=False,
        help_text='Optimal minimum size 800x400px',
    )

    download_report_cover = WagtailImageField()
    download_report_title = models.CharField(max_length=255, null=True, blank=True, default="Download this report")
    download_report_body = models.TextField(null=True, blank=True)
    download_report_button_text = models.CharField(max_length=255, null=True, blank=True, default="Download now")
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        StreamFieldPanel('authors'),
        SnippetChooserPanel('publication_type'),
        FieldPanel('topics'),
        InlinePanel('page_countries', label="Countries"),
        PublishedDatePanel(),
        InlinePanel('publication_datasets', label='Datasets'),
        DownloadsPanel(
            heading='Reports',
            description='Report downloads for this legacy report.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this legacy report.'
        ),
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        MultiFieldPanel(
            [
                FieldPanel('content'),
                FieldPanel('raw_content'),
            ],
            heading='Summary',
            description='Summary for the legacy publication.'
        ),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def publication_downloads_title(self):
        return 'Publication downloads'

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


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['related_pages'] = get_related_pages(
            self.publication_related_links.all(), LegacyPublicationPage.objects)

        return context;


class ShortPublicationPage(HeroMixin, PublishedDateMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, FilteredDatasetMixin, Page):

    class Meta:
        verbose_name = 'Short Publication'

    parent_page_types = ['PublicationIndexPage']
    subpage_types = []

    template = 'publications/publication_chapter_page.html'

    colour = models.CharField(max_length=256, choices=COLOUR_CHOICES, default=RED)
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
        PublicationType, related_name="+", null=True, blank=False, on_delete=models.SET_NULL, verbose_name="Resource Type")
    topics = ClusterTaggableManager(through=ShortPublicationTopic, blank=True, verbose_name="Topics")

    download_report_cover = WagtailImageField()
    download_report_title = models.CharField(max_length=255, null=True, blank=True, default="Download this report")
    download_report_body = models.TextField(null=True, blank=True)
    download_report_button_text = models.CharField(max_length=255, null=True, blank=True, default="Download now")
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('colour'),
        hero_panels(),
        StreamFieldPanel('authors'),
        SnippetChooserPanel('publication_type'),
        FieldPanel('topics'),
        InlinePanel('page_countries', label="Countries"),
        PublishedDatePanel(),
        ContentPanel(),
        InlinePanel('publication_datasets', label='Datasets'),
        DownloadsPanel(
            heading='Downloads',
            description='Downloads for this chapter.'
        ),
        DownloadsPanel(
            related_name='data_downloads',
            heading='Data downloads',
            description='Optional: data download for this chapter.'
        ),
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def publication_downloads_title(self):
        return 'Publication downloads'

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
    def chapter_number(self):
        return 1

    @cached_property
    def chapters(self):
        return [self]

    @cached_property
    def listing_and_appendicies(self):
        return [self]

    @cached_property
    def chapter_word(self):
        return num2words(self.chapter_number)

    @cached_property
    def label_type(self):
        return 'publication'

    @cached_property
    def label(self):
        return 'publication'

    @cached_property
    def label_num(self):
        return 'publication'

    @cached_property
    def sections(self):
        sections = []
        for block in self.content:
            if block.block_type == 'section_heading':
                sections.append(block)
        return sections


class AudioVisualMedia(PublishedDateMixin, TypesetBodyMixin, HeroMixin, SectionBodyMixin, Page):

    """
    Audio Visual page to be used as a child of the Resources Index Page
    """

    template = 'publications/audio_visual_media.html'

    publication_type = models.ForeignKey(
        PublicationType, related_name="+", null=True, blank=False, on_delete=models.SET_NULL, verbose_name="Resource Type")

    participants = StreamField([
        ('internal_participant', PageChooserBlock(
            required=False,
            target_model='ourteam.TeamMemberPage',
            icon='fa-user', label='Internal Participant'
        )),
        ('external_participant', StructBlock([
            ('name', CharBlock(required=False)),
            ('title', CharBlock(required=False)),
            ('photograph', ImageChooserBlock(required=False)),
            ('page', URLBlock(required=False))
        ], icon='fa-user', label='External Participant'))
    ], blank=True, help_text="The people involved in the podcast or webinar")
    topics = ClusterTaggableManager(through=AudioVisualMediaTopic, blank=True, verbose_name="Topics")

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('participants'),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections'),
        FieldPanel('publication_type'),
        FieldPanel('topics'),
        PublishedDatePanel(),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
        InlinePanel('page_notifications', label='Notifications')
    ]

    parent_page_types = ['PublicationIndexPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['related_pages'] = get_related_pages(
            self.publication_related_links.all(), AudioVisualMedia.objects)

        return context

    class Meta:
        verbose_name = 'Audio and Visual Media Page'


class PublicationPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='publication_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]
