import random
import re
from datetime import datetime

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

from di_website.common.base import get_related_pages, hero_panels, Country
from di_website.common.constants import MAX_PAGE_SIZE, MAX_RELATED_LINKS
from di_website.common.mixins import HeroMixin, OtherPageMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.downloads.models import BaseDownload

from .blocks import QuoteStreamBlock, MetaDataDescriptionBlock, MetaDataSourcesBlock


@register_snippet
class Report(ClusterableModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        max_length=255, blank=True, null=True,
        help_text="Optional. Will be auto-generated from title if left blank.")

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('slug'),
    ]

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Report, self).save(**kwargs)


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
    date_of_access = models.DateField(blank=True)
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
        FieldPanel('date_of_access'),
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

    quotes = StreamField(
        QuoteStreamBlock, verbose_name="Quotes", null=True, blank=True)
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


class DatasetPage(TypesetBodyMixin, HeroMixin, Page):
    """ Content of each dataset """

    parent_page_types = ['datasection.DataSetListing']

    publication = models.CharField(
        blank=True, max_length=255, verbose_name='Publication Type',
        help_text='The publication that used this dataset. For a figure, format is [Publication] - [Figure] e.g ITEP 2018 - Figure 1.1')
    release_date = models.DateField(default=datetime.now)
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
    meta_data = StreamField([
        ('description', RichTextBlock(required=True)),
        ('provenance', RichTextBlock()),
        ('variables', RichTextBlock()),
        ('geography', RichTextBlock()),
        ('licence', RichTextBlock()),
        ('citation', RichTextBlock())
    ], verbose_name='Content', help_text='A description is expected, but only one of each shall be shown')
    related_datasets_title = models.CharField(
        blank=True, max_length=255, verbose_name='Title')
    report = models.ForeignKey(
        'datasection.Report', related_name="+", on_delete=models.SET_NULL, blank=True, null=True)
    topics = ClusterTaggableManager(through=DataSetTopic, blank=True, verbose_name="Topics")
    other_pages_heading = models.CharField(
        blank=True, max_length=255, verbose_name='Heading', default='More about')

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('publication'),
        FieldPanel('release_date'),
        StreamFieldPanel('body'),
        StreamFieldPanel('authors'),
        InlinePanel('dataset_downloads', label='Downloads', max_num=None),
        MultiFieldPanel([
            StreamFieldPanel('meta_data'),
            SnippetChooserPanel('report'),
            FieldPanel('topics'),
            InlinePanel('page_countries', label="Countries"),
            InlinePanel('dataset_sources', label='Sources')
        ], heading='Metadata'),
        MultiFieldPanel([
            FieldPanel('related_datasets_title'),
            InlinePanel('related_dataset_links', label="Related Datasets", max_num=MAX_RELATED_LINKS)
        ], heading='Related Dataset'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        content_type = ContentType.objects.get_for_model(DatasetPage)
        context['topics'] = Tag.objects.filter(
                    models.Q(datasection_datasettopic_items__content_object__content_type=content_type)
                ).distinct()
        context['related_datasets'] = get_related_pages(self.related_dataset_links.all(), DatasetPage.objects)
        context['more_about_links'] = get_related_pages(self.more_about_links.all(), DatasetPage.objects)
        context['team_member_links'] = get_related_pages(self.team_member_links.all())

        return context

    @cached_property
    def get_dataset_downloads(self):
        return self.dataset_downloads.all()

    @cached_property
    def get_dataset_sources(self):
        return self.dataset_sources.all()


class DatasetDownloads(BaseDownload, Orderable):
    page = ParentalKey(
        DatasetPage, related_name='dataset_downloads', on_delete=models.CASCADE)


class DatasetPageRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='related_dataset_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [ DatasetPage ])
    ]


class MoreAboutRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='more_about_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]


class TeamMemberRelatedLink(OtherPageMixin):
    page = ParentalKey(Page, related_name='team_member_links', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page', [
            'ourteam.TeamMemberPage'
        ])
    ]


class DataSetSource(models.Model):
    page = ParentalKey(
        DatasetPage, related_name='dataset_sources', on_delete=models.CASCADE)
    source = models.ForeignKey(
        'datasection.DataSource', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='+', verbose_name='Data Source')

    panels = [ SnippetChooserPanel('source') ]



class DataSetListing(TypesetBodyMixin, Page):
    """
    http://development-initiatives.surge.sh/page-templates/21-1-dataset-listing
    """
    class Meta():
        verbose_name = 'DataSet Listing'

    parent_page_types = ['datasection.DataSectionPage']
    sub_page_types = ['dataset.DatasetPage']

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

    def fetch_all_datasets(self):
        return DatasetPage.objects.live();

    def get_context(self, request, *args, **kwargs):
        context = super(DataSetListing, self).get_context(request, *args, **kwargs)

        page = request.GET.get('page', None)
        topic_filter = context['selected_topic'] = request.GET.get('topic', None)
        country_filter = context['selected_country'] = request.GET.get('country', None)
        source_filter = context['selected_source'] = request.GET.get('source', None)
        report_filter = context['selected_report'] = request.GET.get('report', None)

        if not self.is_filtering(request):
            datasets = self.fetch_all_datasets()
            is_filtered = False
        else:
            is_filtered = True
            if topic_filter:
                datasets = DatasetPage.objects.live().filter(topics__slug=topic_filter)
            else:
                datasets = self.fetch_all_datasets()
            if country_filter:
                if 'all--' in country_filter:
                    try:
                        region = re.search('all--(.*)', country_filter).group(1)
                        datasets = datasets.filter(page_countries__country__region__name=region)
                    except AttributeError:
                        pass
                else:
                    datasets = datasets.filter(page_countries__country__slug=country_filter)
            if source_filter:
                datasets = datasets.filter(dataset_sources__source__slug=source_filter)
            if report_filter:
                datasets = datasets.filter(report__slug=report_filter)

        datasets = datasets.order_by('-release_date')
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
            models.Q(datasection_datasettopic_items__content_object__content_type=content_type)
        ).distinct()
        context['countries'] = Country.objects.all()
        context['sources'] = DataSource.objects.all()
        context['reports'] = Report.objects.all()

        return context
