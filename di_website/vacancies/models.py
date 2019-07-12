from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet

from di_website.common.base import StandardPage
from .blocks import VacancyStreamBlock


@register_snippet
class JobDuration(models.Model):
    duration = models.CharField(
        blank=False,
        max_length=100,
        help_text='e.g. Permanent, Full Time, 6 Months, Temp'
    )

    class Meta():
        db_table = 'job_duration'
        verbose_name = 'Job Duration'
        verbose_name_plural = 'Job Durations'

    def __str__(self):
        return self.duration


@register_snippet
class OfficeLocation(models.Model):
    location = models.CharField(
        blank=False,
        max_length=100,
        help_text='e.g. Bristol, UK | Kampala, UG | Nairobi, KE'
    )

    class Meta():
        db_table = 'office_location'
        verbose_name = 'Office Location'
        verbose_name_plural = 'Office Locations'

    def __str__(self):
        return self.location


class VacanciesPage(StandardPage):
    class Meta:
        db_table = 'vacancies_page'
        verbose_name = 'Vacancies Page'

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = [ 'VacancyPage' ]


class VacancyPage(StandardPage):
    vacancy = models.ForeignKey(
        'users.JobTitle',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    duration = models.ForeignKey(
        JobDuration,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    location = models.ForeignKey(
        OfficeLocation,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    salary_scale = models.CharField(blank=True, max_length=255)
    application_close_date = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False
    )
    first_interview_date = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False
    )
    job_start_date = models.DateField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False
    )
    body = StreamField(
        VacancyStreamBlock(),
        verbose_name="Page Body",
        blank=True
    )
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='Other pages in this section'
    )

    content_panels = StandardPage.content_panels + [
        MultiFieldPanel([
            FieldPanel('vacancy'),
            FieldPanel('duration'),
            FieldPanel('location'),
            FieldPanel('salary_scale')
        ], heading='Vacancy Info'),
        MultiFieldPanel([
            FieldPanel('application_close_date'),
            FieldPanel('first_interview_date'),
            FieldPanel('job_start_date')
        ], heading='Dates'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Other Pages')
        ], heading='Other Pages')
    ]

    parent_page_types = [
        'VacanciesPage'
    ]

    class Meta():
        db_table = 'vacancy_page'
        verbose_name = 'Vacancy Page'
