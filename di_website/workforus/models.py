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
        default='Our values'
    )
    value_section_sub_heading = RichTextField(
        blank=True,
        verbose_name='Value Sub-heading',
        help_text='A brief description of the section contents'
    )
    values = StreamField([
        ('value', ValueBlock()),
    ], null=True, blank=True)
    team_story_section_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Section Heading',
        default='Team stories'
    )
    team_story_section_sub_heading = RichTextField(
        blank=True,
        verbose_name='Section Sub-heading',
        help_text='A brief description of the section contents'
    )
    team_stories = StreamField(
        TeamStoryStreamBlock,
        verbose_name="Team Stories",
        null=True,
        blank=True
    )
    vacancy_section_heading = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Section Heading',
        default='Latest vacancies'
    )
    vacancy_section_sub_heading = RichTextField(
        blank=True,
        verbose_name='Section Sub-heading',
        help_text='A brief description of the section contents'
    )
    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('benefits'),
        MultiFieldPanel([
            FieldPanel('value_section_heading'),
            FieldPanel('value_section_sub_heading'),
            StreamFieldPanel('values')
        ], heading='Values Section'),
        MultiFieldPanel([
            FieldPanel('team_story_section_heading'),
            FieldPanel('team_story_section_sub_heading'),
            StreamFieldPanel('team_stories')
        ], heading='Team Stories Section'),
        MultiFieldPanel([
            FieldPanel('vacancy_section_heading'),
            FieldPanel('vacancy_section_sub_heading')
        ], heading='Vacancies Section'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    subpage_types = ['vacancies.VacancyIndexPage', 'general.General']

    def get_context(self, request):
        context = super().get_context(request)
        context['vacancies'] = VacancyPage.objects.live()

        return context
