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

from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel,
    PageChooserPanel, StreamFieldPanel
)
from wagtail.core.blocks import (
    CharBlock, PageChooserBlock, RichTextBlock, StreamBlock, StructBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from di_website.common.base import get_related_pages, hero_panels, other_pages_panel
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS
from di_website.common.mixins import HeroMixin, OtherPageMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.publications.models import Country
from di_website.downloads.models import BaseDownload
from di_website.publications.models import (
    PublicationPage, LegacyPublicationPage, ShortPublicationPage,
    PublicationAppendixPage, PublicationChapterPage, PublicationSummaryPage)

from .blocks import QuoteStreamBlock, MetaDataDescriptionBlock, MetaDataSourcesBlock
from .mixins import DataSetMixin, DataSetSourceMixin
from .panels import metadata_panel


class DataSourceTopic(TaggedItemBase):
    """
    Handles topic tags on the DataSource snippets
    """
    content_object = ParentalKey(
        'datasection.DataSource', on_delete=models.CASCADE, related_name='datasource_topics')


@register_snippet
class DataSource(ClusterableModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    organisation = models.CharField(max_length=255, blank=True)
    link_to_metadata = models.URLField(blank=True)
    geography = models.CharField(max_length=255, blank=True)
    link_to_data = models.URLField(blank=True)
    topics = ClusterTaggableManager(through=DataSourceTopic, blank=True, verbose_name="Topics")
    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        help_text="Optional. Will be auto-generated from title if left blank.")

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('organisation'),
        FieldPanel('link_to_metadata'),
        FieldPanel('link_to_data'),
        FieldPanel('geography'),
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


class DataSectionPage(SectionBodyMixin, TypesetBodyMixin, HeroMixin, Page):
    """ Main page for datasets """

    quotes = StreamField(QuoteStreamBlock, verbose_name="Quotes", null=True, blank=True)
    dataset_info = models.TextField(
        null=False, blank=False, default="", help_text='A description of the datasets')
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')

    content_panels = Page.content_panels + [
        hero_panels(allowed_pages=['datasection.DataSetListing']),
        StreamFieldPanel('body'),
        StreamFieldPanel('quotes'),
        FieldPanel('dataset_info'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')

    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['general.General', 'datasection.DataSetListing']

    class Meta:
        verbose_name = "Data Section Page"

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
        context['dataset_count'] = DatasetPage.objects.live().count()
        return context


class DataSetTopic(TaggedItemBase):
    content_object = ParentalKey(
        'datasection.DatasetPage', on_delete=models.CASCADE, related_name='dataset_topics')


class DatasetPage(DataSetMixin, TypesetBodyMixin, HeroMixin, Page):
    """ Content of each dataset """

    class Meta():
        verbose_name = 'Data Set Page'

    related_datasets_title = models.CharField(
        blank=True, max_length=255, default='Related datasets', verbose_name='Section Title')
    topics = ClusterTaggableManager(through=DataSetTopic, blank=True, verbose_name="Topics")

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('release_date'),
        StreamFieldPanel('body'),
        StreamFieldPanel('authors'),
        InlinePanel('dataset_downloads', label='Downloads', max_num=None),
        metadata_panel(),
        MultiFieldPanel([
            FieldPanel('related_datasets_title'),
            InlinePanel('related_datasets', label="Related Datasets")
        ], heading='Related Datasets'),
        other_pages_panel()
    ]

    def get_context(self, request):
        context = super().get_context(request)

        content_type = ContentType.objects.get_for_model(DatasetPage)
        context['topics'] = Tag.objects.filter(
                models.Q(datasection_datasettopic_items__content_object__content_type=content_type)
            ).distinct()
        context['related_datasets'] = get_related_pages(
            self.related_datasets.all(), DatasetPage.objects)
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

        for report in reports:
            figures = Page.objects.live().filter(
                figurepage__figure_datasets__dataset__slug=self.slug,
                figurepage__publication__slug=report.slug
            ).specific()
            report.figures = figures

        return reports


class DatasetDownloads(Orderable, BaseDownload):
    page = ParentalKey(
        DatasetPage, related_name='dataset_downloads', on_delete=models.CASCADE)


class DatasetPageRelatedLink(OtherPageMixin):
    page = ParentalKey(DatasetPage, related_name='related_datasets', on_delete=models.CASCADE)

    panels = [PageChooserPanel('other_page', [DatasetPage])]


class DataSetSource(DataSetSourceMixin):
    page = ParentalKey(DatasetPage, related_name='dataset_sources', on_delete=models.CASCADE)


class FigureTopic(TaggedItemBase):
    content_object = ParentalKey(
        'datasection.FigurePage', on_delete=models.CASCADE, related_name='figure_topics')


class FigurePage(DataSetMixin, TypesetBodyMixin, HeroMixin, Page):
    """ Content of each figure """

    class Meta():
        verbose_name = 'Figure Page'

    name = models.CharField(
        blank=True, max_length=255, verbose_name='Name',
        help_text='The name of this figure in the publication e.g Figure 1.1')
    publication = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="The publication in which this figure appears"
    )
    related_figures_title = models.CharField(
        blank=True, max_length=255, default='Related figures', verbose_name='Section Title')
    topics = ClusterTaggableManager(through=FigureTopic, blank=True, verbose_name="Topics")

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('name'),
        FieldPanel('release_date'),
        PageChooserPanel('publication', [
            'publications.PublicationPage',
            'publications.ShortPublicationPage',
            'publications.LegacyPublicationPage',
            'publications.PublicationSummaryPage',
            'publications.PublicationChapterPage',
            'publications.PublicationAppendixPage'
        ]),
        StreamFieldPanel('body'),
        StreamFieldPanel('authors'),
        InlinePanel('figure_downloads', label='Downloads', max_num=None),
        metadata_panel(sources_relation='figure_sources'),
        InlinePanel('figure_datasets', label='Data Sets'),
        MultiFieldPanel([
            FieldPanel('related_figures_title'),
            InlinePanel('related_figures', label="Related Figures")
        ], heading='Related Figures'),
        other_pages_panel()
    ]

    def get_context(self, request):
        context = super().get_context(request)

        content_type = ContentType.objects.get_for_model(DatasetPage)
        context['topics'] = Tag.objects.filter(
                models.Q(datasection_figuretopic_items__content_object__content_type=content_type)
            ).distinct()
        context['related_figures'] = get_related_pages(
            self.related_figures.all(), FigurePage.objects)

        return context

    @cached_property
    def get_figure_downloads(self):
        return self.figure_downloads.all()

    @cached_property
    def get_figure_sources(self):
        return self.figure_sources.all()

    def get_name(self):
        return self.publication.title + ' - ' + self.name if self.publication else self.name


class FigurePageDownloads(Orderable, BaseDownload):
    page = ParentalKey(FigurePage, related_name='figure_downloads', on_delete=models.CASCADE)


class FigurePageRelatedLink(OtherPageMixin):
    page = ParentalKey(FigurePage, related_name='related_figures', on_delete=models.CASCADE)

    panels = [PageChooserPanel('other_page', [FigurePage])]


class FigureDataSet(Orderable):
    page = ParentalKey(FigurePage, related_name='figure_datasets', on_delete=models.CASCADE)
    dataset = models.ForeignKey(
        'datasection.DatasetPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Data Set',
        help_text='A dataset on which this figure is based')

    panels = [PageChooserPanel('dataset', [DatasetPage])]


class FigureSource(DataSetSourceMixin):
    page = ParentalKey(FigurePage, related_name='figure_sources', on_delete=models.CASCADE)


class DataSetListing(TypesetBodyMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/21-1-dataset-listing
    """
    class Meta():
        verbose_name = 'DataSet Listing'

    parent_page_types = ['datasection.DataSectionPage']
    subpage_types = ['datasection.DatasetPage', 'datasection.FigurePage']

    hero_text = RichTextField(
        null=True, blank=True, help_text='A description of the page content')
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')

    content_panels = Page.content_panels + [
        FieldPanel('hero_text'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')
    ]

    def is_filtering(self, request):
        get = request.GET.get
        return get('topic', None) or get('country', None) or get('source', None) or get('report', None)

    def fetch_all_data(self):
        dataset_content_type = ContentType.objects.get_for_model(DatasetPage)
        figures_content_type = ContentType.objects.get_for_model(FigurePage)
        return Page.objects.live().filter(
            models.Q(content_type=dataset_content_type) |
            models.Q(content_type=figures_content_type)
        ).specific()

    def fetch_filtered_data(self, context):
        dataset_content_type = ContentType.objects.get_for_model(DatasetPage)
        figures_content_type = ContentType.objects.get_for_model(FigurePage)
        topic = context['selected_topic']
        country = context['selected_country']
        source = context['selected_source']
        report = context['selected_report']

        if topic:
            datasets = Page.objects.live().filter(
                models.Q(content_type=dataset_content_type) |
                models.Q(content_type=figures_content_type),
                models.Q(datasetpage__topics__slug=topic) |
                models.Q(figurepage__topics__slug=topic)
            ).specific()
        else:
            datasets = self.fetch_all_data()
        if country:
            if 'all--' in country:
                try:
                    region = re.search('all--(.*)', country).group(1)
                    datasets = datasets.filter(
                        models.Q(datasetpage__page_countries__country__region__name=region) |
                        models.Q(figurepage__page_countries__country__region__name=region))
                except AttributeError:
                    pass
            else:
                datasets = datasets.filter(
                    models.Q(datasetpage__page_countries__country__slug=country) |
                    models.Q(figurepage__page_countries__country__slug=country))
        if source:
            datasets = datasets.filter(
                models.Q(datasetpage__dataset_sources__source__slug=source) |
                models.Q(figurepage__figure_sources__source__slug=source))
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
                for dataset in pubs.specific.publication_datasets.all():
                    results = datasets.filter(
                        models.Q(datasetpage__slug__exact=dataset.dataset.slug) |
                        models.Q(figurepage__slug__exact=dataset.dataset.slug))
                    if results:
                        datasets = results
            else:
                datasets = None

        return datasets

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

        content_type = ContentType.objects.get_for_model(DatasetPage)
        context['topics'] = Tag.objects.filter(
            datasection_datasettopic_items__content_object__content_type=content_type
        ).distinct()
        context['countries'] = Country.objects.all()
        context['sources'] = DataSource.objects.all()

        context['reports'] = Page.objects.live().filter(
            models.Q(publicationpage__publication_datasets__dataset__content_type=content_type) |
            models.Q(publicationsummarypage__publication_datasets__dataset__content_type=content_type) |
            models.Q(legacypublicationpage__publication_datasets__dataset__content_type=content_type) |
            models.Q(publicationappendixpage__publication_datasets__dataset__content_type=content_type) |
            models.Q(publicationchapterpage__publication_datasets__dataset__content_type=content_type) |
            models.Q(shortpublicationpage__publication_datasets__dataset__content_type=content_type)
        ).distinct()

        return context
