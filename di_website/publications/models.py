from num2words import num2words
from itertools import chain
import operator
from functools import reduce

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
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel


from di_website.common.base import hero_panels, get_paginator_range
from di_website.common.mixins import HeroMixin, OtherPageMixin
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS
from di_website.downloads.utils import DownloadsPanel

from taggit.models import Tag, TaggedItemBase

from .mixins import (
    FlexibleContentMixin, UniquePageMixin, PageSearchMixin, LegacyPageSearchMixin, ParentPageSearchMixin,
    PublishedDateMixin, UUIDMixin, ReportChildMixin, FootnoteMixin)
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
        hero_panels(),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['PublicationPage', 'LegacyPublicationPage', 'ShortPublicationPage', 'general.General']
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
            stories = stories.filter(page_countries__country__slug=country_filter)
            legacy_pubs = legacy_pubs.filter(page_countries__country__slug=country_filter)
            short_pubs = short_pubs.filter(page_countries__country__slug=country_filter)

        if search_filter:
            if stories:
                child_count = reduce(operator.add, [len(pub.get_children()) for pub in stories])
                if child_count:
                    pub_children = reduce(operator.or_, [pub.get_children() for pub in stories]).live().specific().search(search_filter)
                    if pub_children:
                        matching_parents = reduce(operator.or_, [stories.parent_of(child) for child in pub_children])
                        stories = list(chain(stories.search(search_filter), matching_parents))
                    else:
                        stories = stories.search(search_filter)
                else:
                    stories = stories.search(search_filter)
            legacy_pubs = legacy_pubs.search(search_filter)
            short_pubs = short_pubs.search(search_filter)

        story_list = list(chain(stories, legacy_pubs, short_pubs))
        story_list.sort(key=lambda x: x.published_date, reverse=True)
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
        context['selected_topic'] = topic_filter
        context['countries'] = Country.objects.all()
        context['selected_country'] = country_filter
        context['search_filter'] = search_filter
        context['is_filtered'] = search_filter or topic_filter or country_filter
        context['paginator_range'] = get_paginator_range(paginator, context['stories'])

        return context

    class Meta():
        verbose_name = 'Publication Index Page'


class PublicationPage(HeroMixin, PublishedDateMixin, ParentPageSearchMixin, UUIDMixin, Page):

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
        PublicationType, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
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
        InlinePanel('page_countries', label="Countries"),
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


class PublicationSummaryPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UniquePageMixin, UUIDMixin, FootnoteMixin, Page):

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
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        StreamFieldPanel('footnotes_list'),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
    ]

    @cached_property
    def label(self):
        return 'The summary'

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


class PublicationChapterPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, FootnoteMixin, Page):

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
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        StreamFieldPanel('footnotes_list'),
        InlinePanel('page_notifications', label='Notifications'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS),
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


class PublicationAppendixPage(HeroMixin, ReportChildMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, FootnoteMixin, Page):

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


class LegacyPublicationPage(HeroMixin, PublishedDateMixin, LegacyPageSearchMixin, FootnoteMixin, Page):

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
        PublicationType, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    topics = ClusterTaggableManager(through=LegacyPublicationTopic, blank=True, verbose_name="Topics")

    raw_content = models.TextField(null=True, blank=True)
    content = RichTextField(
        help_text='Content for the legacy report',
        null=True, blank=True
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
        StreamFieldPanel('footnotes_list'),
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


class ShortPublicationPage(HeroMixin, PublishedDateMixin, FlexibleContentMixin, PageSearchMixin, UUIDMixin, FootnoteMixin, Page):

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
        PublicationType, related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
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
        MultiFieldPanel([
            FieldPanel('download_report_title'),
            FieldPanel('download_report_body'),
            ImageChooserPanel('download_report_cover'),
            DocumentChooserPanel('report_download')
        ], heading='Report download section'),
        StreamFieldPanel('footnotes_list'),
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


class PublicationPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='publication_related_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]
