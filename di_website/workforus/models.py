from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet

from di_website.common.base import hero_panels
from di_website.common.mixins import BaseStreamBodyMixin, HeroMixin
from di_website.vacancies.models import VacancyPage
from .blocks import BenefitsStreamBlock, TeamStoryStreamBlock

from modelcluster.fields import ParentalKey


@register_snippet
class Values(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Value Name',)
    paragraph = models.TextField(max_length=255, verbose_name='Description',)
    panels = [
        FieldPanel('title'),
        FieldPanel('paragraph'),
    ]

    class Meta():
        verbose_name = 'Our Value'
        verbose_name_plural = 'Our Values'

    def __str__(self):
        return self.title


class WorkForUsPage(BaseStreamBodyMixin, HeroMixin, Page):
    class Meta():
        verbose_name = 'Work For Us Page'

    recruitment_policy = models.URLField(
        null=True,
        blank=True,
        verbose_name='Recruitment Policy',
        help_text='A Link to the recruitment policy if any'
    )
    gdr_policy = models.URLField(
        null=True,
        blank=True,
        verbose_name='GDPR Policy',
        help_text='A Link to the GDPR policy if any'
    )
    benefits = StreamField(
        BenefitsStreamBlock,
        verbose_name="Benefits",
        null=True,
        blank=True
    )
    logos = StreamField(
        [('image', ImageChooserBlock())],
        verbose_name="Logos",
        null=True,
        blank=True
    )
    values_text = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Brief text for values section',
    )
    team_story_heading = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Brief descriptive text',
    )
    team_story = StreamField(
        TeamStoryStreamBlock,
        verbose_name="Team Stories",
        null=True,
        blank=True
    )
    vacancy_heading = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Brief descriptive text for vacancies',
    )
    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        FieldPanel('recruitment_policy'),
        FieldPanel('gdr_policy'),
        StreamFieldPanel('benefits'),
        StreamFieldPanel('logos'),
        FieldPanel('values_text'),
        MultiFieldPanel([
            FieldPanel('team_story_heading'),
            StreamFieldPanel('team_story'),
        ], heading='Team Stories'),
        FieldPanel('vacancy_heading')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['vacancies'] = VacancyPage.objects.live()
        return context
