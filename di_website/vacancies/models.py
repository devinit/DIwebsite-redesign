from django.db import models, DataError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet

from di_website.common.base import BaseStreamBody, StandardPage
from di_website.users.models import Department, Subscription


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

    class Meta():
        db_table = 'office_location'
        verbose_name = 'Office Location'
        verbose_name_plural = 'Office Locations'

    def __str__(self):
        return self.location


class VacancyIndexPage(StandardPage):
    """
    Shows a list of available vacancies
    """
    class Meta:
        db_table = 'vacancies_page'
        verbose_name = 'Vacancy Index Page'

    parent_page_types = ['home.HomePage']
    subpage_types = ['VacancyPage']

    def create_subscription(self, email, subscription_on, department):
        subscription = Subscription.objects.create_subscription(email, 'jobs', department)
        subscription.save()

        return subscription

    def get_context(self, request):
        context = super().get_context(request)

        all_departments = Department.objects.all()
        context['vacancies'] = VacancyPage.objects.live()
        context['departments'] = all_departments

        form = {'success': False}
        email = {
            'id': 'email_address',
            'label': 'Email address',
            'placeholder': 'Your email address'
        }
        if request.method == 'POST':
            data = request.POST.copy()
            email_address = data.get('email_address', None)
            email['value'] = email_address
            try:
                if email_address:
                    validate_email(email_address)

                    monitored_departments = []
                    for department in all_departments:
                        if data.get(department.slug, None) == 'on':
                            monitored_departments.append(department)

                    form['alert_message'] = 'You have signed up for vacancy alerts for '
                    if len(monitored_departments):
                        first = True
                        for department in monitored_departments:
                            self.create_subscription(email.value, 'jobs', department)
                            if first:
                                form['alert_message'] = form.get('alert_message') + ' ' + department.name
                                first = False
                            else:
                                form['alert_message'] = form.get('alert_message') + ', ' + department.name
                    else:
                        for department in all_departments:
                            self.create_subscription(email.value, 'jobs', department)
                        form['alert_message'] = ' all departments'

                    form['success'] = True
                else:
                    email['field_error'] = 'This field is required'
            except ValidationError:
                email['field_error'] = 'Invalid email'
            except DataError:
                email['field_error'] = 'Email address too long'

        form['email'] = email
        context['form'] = form

        return context


class VacancyPage(StandardPage, BaseStreamBody):
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
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='Other pages in this section'
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
            FieldPanel('downloads_title'),
            FieldPanel('downloads_description'),
            InlinePanel('page_downloads', label='Download', max_num=None)
        ], heading='Downloads'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Other Pages')
        ], heading='Other Pages')
    ]

    parent_page_types = [
        'VacancyIndexPage'
    ]


    @cached_property
    def get_page_downloads(self):
        return self.page_downloads.all()

    class Meta():
        db_table = 'vacancy_page'
        verbose_name = 'Vacancy Page'
