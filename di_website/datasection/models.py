import random
import re
from datetime import datetime
from itertools import chain

from django.db import models
from django.utils.text import slugify
from django.utils.functional import cached_property
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import Tag, TaggedItemBase

from wagtail.admin.panels import (
    FieldPanel, InlinePanel, MultiFieldPanel,
    PageChooserPanel
)
from wagtail.blocks import CharBlock, PageChooserBlock, StructBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from wagtail.snippets.models import register_snippet

from di_website.common.base import get_paginator_range, hero_panels, other_pages_panel
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS, RICHTEXT_FEATURES_NO_FOOTNOTES
from di_website.common.mixins import HeroMixin, OtherPageMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.common.blocks import BannerBlock
from di_website.publications.fields import AdvancedInteractiveChartBlock
from di_website.publications.models import Country
from di_website.downloads.models import BaseDownload

from .blocks import QuoteStreamBlock
from .mixins import DataSetMixin, DataSetSourceMixin
from .panels import metadata_panel

from wagtailmetadata.models import MetadataPageMixin


class DatasetListingMetadataPageMixin(MetadataPageMixin):
    max_count = 1

    class Meta:
        abstract = True

    def get_meta_image(self):
        if getattr(self.specific, 'search_image', None):
            return self.specific.search_image
        return super(DatasetListingMetadataPageMixin, self).get_meta_image()

    def get_meta_description(self):
        return self.search_description if self.search_description else self.title

    def get_meta_title(self):
        return self.title


def get_related_dataset_pages(selected_pages, dataset_page, min_len=MAX_RELATED_LINKS):
    count = len(selected_pages)
    sources = dataset_page.dataset_sources.all()
    queryset = Page.objects.none()
    for dataset_source in sources:
        filtered_queryset = Page.objects.sibling_of(dataset_page).live().exclude(id=dataset_page.id).filter(datasetpage__dataset_sources__source__slug=dataset_source.source.slug)
        queryset = queryset | filtered_queryset
    queryset = queryset.distinct()

    if count < min_len:
        difference = min_len - count
        related_pages = [link.other_page for link in selected_pages]
        if related_pages and queryset:
            id_list = [page.id for page in related_pages if page]
            if id_list:
                return list(related_pages) + list(queryset.live().exclude(id__in=id_list)[:difference])
            return list(queryset.live()[:min_len])
        elif queryset:
            return list(queryset.live()[:min_len])

    return list([link.other_page for link in selected_pages])


class DataSourceTopic(TaggedItemBase):
    """
    Handles topic tags on the DataSource snippets
    """
    content_object = ParentalKey(
        'datasection.DataSource', on_delete=models.CASCADE, related_name='datasource_topics')


@register_snippet
class DataSource(ClusterableModel):
    source_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    title = models.TextField(unique=True)
    authors = StreamField([
        ('internal_author', PageChooserBlock(
            required=False,
            target_model='ourteam.TeamMemberPage',
            icon='heroicons-user-solid'
        )),
        ('external_author', StructBlock([
            ('name', CharBlock(required=False)),
            ('title', CharBlock(required=False)),
            ('photograph', ImageChooserBlock(required=False)),
            ('page', URLBlock(required=False))
        ], icon='heroicons-user-solid'))
    ], blank=True, use_json_field=True)
    description = models.TextField(blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    link_to_metadata = models.URLField(blank=True)
    link_to_data = models.URLField(blank=True)
    geography = models.TextField(blank=True, null=True)
    date_of_access = models.DateField(null=True, blank=True)
    internal_notes = models.TextField(blank=True, null=True)
    licence = models.TextField(max_length=255, blank=True, null=True)
    topics = ClusterTaggableManager(through=DataSourceTopic, blank=True, verbose_name="Topics")
    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        help_text="Optional. Will be auto-generated from title if left blank.")

    panels = [
        FieldPanel('source_id'),
        FieldPanel('title'),
        FieldPanel('authors'),
        FieldPanel('description'),
        FieldPanel('organisation'),
        FieldPanel('link_to_metadata'),
        FieldPanel('link_to_data'),
        FieldPanel('geography'),
        FieldPanel('date_of_access'),
        FieldPanel('internal_notes'),
        FieldPanel('topics'),
        FieldPanel('slug'),
    ]

    class Meta:
        ordering = ["title"]
        verbose_name = 'Data Source'
        verbose_name_plural = 'Data Sources'

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(DataSource, self).save(**kwargs)


class DataSectionPage(TypesetBodyMixin, HeroMixin, Page):
    """ Main page for datasets """

    quotes = StreamField(QuoteStreamBlock, verbose_name="Quotes", null=True, blank=True, use_json_field=True)
    dataset_info = RichTextField(
        null=True, blank=True,
        help_text='A description of the datasets',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES)
    tools = StreamField(
        [
            ('tool', BannerBlock(template='datasection/tools_banner_block.html')),
            ('advanced_interactive_chart', AdvancedInteractiveChartBlock(template='datasection/interactive_chart.html')),
        ],
        verbose_name="Tools", null=True, blank=True, use_json_field=True)
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')

    content_panels = Page.content_panels + [
        hero_panels(allowed_pages=['datasection.DataSetListing']),
        FieldPanel('body'),
        FieldPanel('dataset_info'),
        FieldPanel('tools'),
        FieldPanel('quotes'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        'general.General',
        'datasection.DataSetListing',
        'spotlight.SpotlightPage',
        'publications.ShortPublicationPage'
    ]

    class Meta:
        verbose_name = "Data Section Page"

    @cached_property
    def get_dataset_listing_page(self):
        dataset_listing = self.get_children().type(DataSetListing)
        return dataset_listing[0] if dataset_listing else None

    def count_quotes(self):
        quote_counter = 0
        for quote in self.quotes:
            quote_counter = quote_counter + 1
        return quote_counter

    def get_random_quote(self):
        number_of_quotes = self.count_quotes()
        if number_of_quotes == 1:
            for quote in self.quotes:
                return quote
        elif number_of_quotes >= 2:
            random_number = random.randint(0, number_of_quotes - 1)
            for index, quote in enumerate(self.quotes):
                if random_number == index:
                    return quote
        return

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['random_quote'] = self.get_random_quote()
        context['dataset_count'] = DatasetPage.objects.descendant_of(self).live().count()
        return context


class DatasetPage(DataSetMixin, TypesetBodyMixin, HeroMixin, Page):
    """ Content of each dataset """

    class Meta():
        verbose_name = 'Data Set Page'

    dataset_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    dataset_title = models.TextField(unique=True, blank=True, null=True)
    related_datasets_title = models.CharField(
        blank=True, max_length=255, default='Related datasets', verbose_name='Section Title')

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('dataset_id'),
        FieldPanel('dataset_title'),
        FieldPanel('release_date'),
        FieldPanel('body'),
        FieldPanel('authors'),
        InlinePanel('dataset_downloads', label='Downloads', max_num=None),
        metadata_panel(),
        MultiFieldPanel([
            FieldPanel('related_datasets_title'),
            InlinePanel('related_datasets', label="Related Datasets")
        ], heading='Related Datasets'),
        other_pages_panel(),
        InlinePanel('page_notifications', label='Notifications')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['topics'] = [orderable.topic for orderable in self.dataset_topics.all()]
        context['related_datasets'] = get_related_dataset_pages(
            self.related_datasets.all(), self)
        context['reports'] = self.get_usages()

        return context

    @cached_property
    def get_dataset_downloads(self):
        return self.dataset_downloads.all()

    @cached_property
    def get_dataset_sources(self):
        return self.dataset_sources.all()

    def get_usages(self):
        reports = Page.objects.live().filter(
            models.Q(publicationpage__publication_datasets__dataset__slug=self.slug) |
            models.Q(legacypublicationpage__publication_datasets__dataset__slug=self.slug) |
            models.Q(publicationsummarypage__publication_datasets__dataset__slug=self.slug) |
            models.Q(publicationchapterpage__publication_datasets__dataset__slug=self.slug) |
            models.Q(publicationappendixpage__publication_datasets__dataset__slug=self.slug) |
            models.Q(shortpublicationpage__publication_datasets__dataset__slug=self.slug)
        ).specific()

        return reports

    def get_download_name(self):
        return self.title


@register_snippet
class DataTopic(ClusterableModel):
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
        verbose_name_plural = 'Data topics'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(DataTopic, self).save(*args, **kwargs)


class DatasetPageTopic(Orderable):
    page = ParentalKey(
        DatasetPage, related_name='dataset_topics', on_delete=models.CASCADE)

    topic = models.ForeignKey(
        DataTopic, related_name="+", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic.name


class DatasetDownloads(Orderable, BaseDownload):
    page = ParentalKey(
        DatasetPage, related_name='dataset_downloads', on_delete=models.CASCADE)


class DatasetPageRelatedLink(OtherPageMixin):
    page = ParentalKey(DatasetPage, related_name='related_datasets', on_delete=models.CASCADE)

    panels = [PageChooserPanel('other_page', [DatasetPage])]


class DataSetSource(DataSetSourceMixin):
    page = ParentalKey(DatasetPage, related_name='dataset_sources', on_delete=models.CASCADE)


class DataSetListing(DatasetListingMetadataPageMixin, TypesetBodyMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/21-1-dataset-listing
    """
    class Meta():
        verbose_name = 'DataSet Listing'

    parent_page_types = ['datasection.DataSectionPage']
    subpage_types = ['datasection.DatasetPage']

    hero_text = RichTextField(
        null=True, blank=True, help_text='A description of the page content', features=RICHTEXT_FEATURES_NO_FOOTNOTES)
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')

    content_panels = Page.content_panels + [
        FieldPanel('hero_text'),
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')
    ]

    def is_filtering(self, request):
        get = request.GET.get
        return get('topic', None) or get('country', None) or get('source', None) or get('report', None)

    def fetch_all_data(self):
        return DatasetPage.objects.live().specific()

    def fetch_filtered_data(self, context):
        topic = context['selected_topic']
        country = context['selected_country']
        source = context['selected_source']
        report = context['selected_report']

        if topic:
            datasets = DatasetPage.objects.live().specific().filter(dataset_topics__topic__slug=topic)
        else:
            datasets = self.fetch_all_data()
        if country:
            if 'all--' in country:
                try:
                    region = re.search('all--(.*)', country).group(1)
                    datasets = datasets.filter(page_countries__country__region__name=region)
                except AttributeError:
                    pass
            else:
                datasets = datasets.filter(page_countries__country__slug=country)
        if source:
            datasets = datasets.filter(dataset_sources__source__slug=source)
        if report:
            pubs = Page.objects.filter(
                models.Q(publicationpage__publication_datasets__item__slug=report) |
                models.Q(publicationsummarypage__publication_datasets__item__slug=report) |
                models.Q(publicationappendixpage__publication_datasets__item__slug=report) |
                models.Q(publicationchapterpage__publication_datasets__item__slug=report) |
                models.Q(legacypublicationpage__publication_datasets__item__slug=report) |
                models.Q(shortpublicationpage__publication_datasets__item__slug=report)
            ).first()
            if (pubs and pubs.specific.publication_datasets):
                filtered_datasets = Page.objects.none()
                for dataset in pubs.specific.publication_datasets.all():
                    results = datasets.filter(slug__exact=dataset.dataset.slug)
                    if results:
                        filtered_datasets = filtered_datasets | results
                datasets = filtered_datasets
            else:
                datasets = None

        return datasets

    def get_active_countries(self):
        active_countries = []
        datasets = DatasetPage.objects.all()

        for dataset in datasets:
            countries = dataset.page_countries.all()
            for country in countries:
                active_country = Country.objects.get(id=country.country_id)
                if active_country not in active_countries:
                    active_countries.append(active_country)
        return active_countries

    def get_context(self, request, *args, **kwargs):
        context = super(DataSetListing, self).get_context(request, *args, **kwargs)

        page = request.GET.get('page', None)
        context['selected_topic'] = request.GET.get('topic', None)
        context['selected_country'] = request.GET.get('country', None)
        context['selected_source'] = request.GET.get('source', None)
        context['selected_report'] = request.GET.get('report', None)

        if not self.is_filtering(request):
            datasets = self.fetch_all_data()
            is_filtered = False
        else:
            is_filtered = True
            datasets = self.fetch_filtered_data(context)

        datasets = datasets.order_by('-first_published_at') if datasets else []
        context['is_filtered'] = is_filtered
        paginator = Paginator(datasets, MAX_PAGE_SIZE)
        try:
            context['datasets'] = paginator.page(page)
        except PageNotAnInteger:
            context['datasets'] = paginator.page(1)
        except EmptyPage:
            context['datasets'] = paginator.page(paginator.num_pages)

        context['paginator_range'] = get_paginator_range(paginator, context['datasets'])

        context['topics'] = [page_orderable.topic for page_orderable in DatasetPageTopic.objects.all().order_by('topic__name') if page_orderable.page.live]
        context['countries'] = self.get_active_countries()
        context['sources'] = DataSource.objects.all()

        context['reports'] = Page.objects.live().filter(
            models.Q(publicationpage__publication_datasets__isnull=False) |
            models.Q(publicationsummarypage__publication_datasets__isnull=False) |
            models.Q(publicationappendixpage__publication_datasets__isnull=False) |
            models.Q(legacypublicationpage__publication_datasets__isnull=False) |
            models.Q(publicationchapterpage__publication_datasets__isnull=False) |
            models.Q(shortpublicationpage__publication_datasets__isnull=False)
        ).distinct().order_by('title')

        return context
