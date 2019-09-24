from django.db import models

from wagtail.core.blocks import (
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock
)

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
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from di_website.common.base import hero_panels
from di_website.common.blocks import ValueBlock
from di_website.common.mixins import TypesetBodyMixin, HeroMixin
from di_website.vacancies.models import VacancyPage
from .blocks import BenefitsStreamBlock, TeamStoryStreamBlock

from modelcluster.fields import ParentalKey


class WorkForUsPage(TypesetBodyMixin, HeroMixin, Page):
    class Meta():
        verbose_name = 'Work For Us Page'

    benefits = StreamField(
        BenefitsStreamBlock,
        verbose_name="Benefits",
        null=True,
        blank=True
    )

    value_section_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Value Heading',
    )
    value_section_sub_heading = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Value Sub Heading',
    )
    values = StreamField([
        ('value', ValueBlock()),
    ], null=True, blank=True)

    team_story = StreamField(
        TeamStoryStreamBlock,
        verbose_name="Team Stories",
        null=True,
        blank=True
    )
    vacancy_title = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Vacancy Title',
    )
    vacancy_subtitle_text = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Brief descriptive text for vacancies',
    )
    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('benefits'),
        FieldPanel('value_section_heading'),
        FieldPanel('value_section_sub_heading'),
        StreamFieldPanel('values'),
        StreamFieldPanel('team_story'),
        FieldPanel('vacancy_title'),
        FieldPanel('vacancy_subtitle_text'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['vacancies.VacancyIndexPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['vacancies'] = VacancyPage.objects.live()
        return context
