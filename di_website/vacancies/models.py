from django.db import models
from django.utils.functional import cached_property

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Page, Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES

from modelcluster.fields import ParentalKey


@register_snippet
class OfficeLocation(models.Model):
    """
    Keeps things uniform; better than freetext
    """
    location = models.CharField(
        blank=False,
        max_length=100,
        help_text='e.g. Bristol, UK | Kampala, UG | Nairobi, KE'
    )
    address = RichTextField(
        blank=True,
        null=True,
        help_text="E.g. 'North Quay House Quay Side, Temple Back Bristol, BS1 6FL, UK'",
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
    )
    contact = models.CharField(
        blank=True,
        max_length=255,
        help_text="E.g. '+44 (0) 1179 272 505'"
    )
    longitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=9,
        decimal_places=6
    )
    latitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=9,
        decimal_places=6
    )

    class Meta():
        db_table = 'office_location'
        verbose_name = 'Office Location'
        verbose_name_plural = 'Office Locations'

    def __str__(self):
        return self.location


class VacancyIndexPage(HeroMixin, Page):
    """
    Shows a list of available vacancies
    """
    class Meta:
        db_table = 'vacancies_page'
        verbose_name = 'Vacancy Index Page'

    parent_page_types = ['workforus.WorkForUsPage']
    subpage_types = ['VacancyPage','general.General']

    def get_context(self, request):
        context = super().get_context(request)
        context['vacancies'] = VacancyPage.objects.live()
        return context

    email_alert_confirmation_label = RichTextField(
        blank=True,
        verbose_name='Descriptive Text for Consent to Email Alerts',
        default='By checking this box you consent to us collecting the data submitted',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('email_alert_confirmation_label'),
        InlinePanel('page_notifications', label='Notifications')
    ]


class VacancyPage(TypesetBodyMixin, SectionBodyMixin, HeroMixin, Page):
    vacancy = models.ForeignKey(
        'users.JobTitle',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    duration = models.CharField(null=True, max_length=255)
    location = models.ForeignKey(
        OfficeLocation,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    salary_scale = models.CharField(blank=True, max_length=255)
    application_close = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False
    )
    first_interview = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )
    second_interview = models.CharField(
        blank=True,
        null=True,
        max_length=255
    )
    job_start = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False
    )
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='Learn more about Development Initiatives'
    )
    downloads_title = models.CharField(
        blank=True,
        max_length=255,
        default='Apply for this position',
        verbose_name='Title',
        help_text='Title for the downloads section on a vacancy page'
    )
    downloads_description = RichTextField(
        blank=True,
        verbose_name='Description',
        help_text='Optional: a brief description of what to do in this section',
        features=RICHTEXT_FEATURES_NO_FOOTNOTES
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            FieldPanel('vacancy'),
            FieldPanel('duration'),
            FieldPanel('location'),
            FieldPanel('salary_scale')
        ], heading='Vacancy Info'),
        MultiFieldPanel([
            FieldPanel('application_close'),
            FieldPanel('first_interview'),
            FieldPanel('second_interview'),
            FieldPanel('job_start')
        ], heading='Dates'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('downloads_title'),
            FieldPanel('downloads_description'),
            InlinePanel('page_downloads', label='Download', max_num=None)
        ], heading='Downloads'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Other Pages')
        ], heading='Other Pages'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['general.General']
    parent_page_types = [
        'VacancyIndexPage'
    ]

    @cached_property
    def get_page_downloads(self):
        return self.page_downloads.all()

    class Meta():
        db_table = 'vacancy_page'
        verbose_name = 'Vacancy Page'


class VacancyDownload(Orderable):
    page = ParentalKey(
        VacancyPage, related_name='page_downloads', on_delete=models.CASCADE
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: document title, defaults to the file name if left blank',
    )

    @cached_property
    def get_title(self):
        return self.title if self.title else self.file.title

    def __str__(self):
        return self.get_title

    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title')
    ]
