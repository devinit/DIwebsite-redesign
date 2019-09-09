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
from di_website.common.mixins import TypesetBodyMixin, HeroMixin
from di_website.vacancies.models import VacancyPage
from .blocks import BenefitsStreamBlock, TeamStoryStreamBlock

from modelcluster.fields import ParentalKey


@register_snippet
class Values(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Name',)
    excerpt = models.TextField(max_length=255, verbose_name='Description',)
    panels = [
        FieldPanel('title'),
        FieldPanel('excerpt'),
    ]

    class Meta():
        verbose_name = 'Our Value'
        verbose_name_plural = 'Our Values'

    def __str__(self):
        return self.title


class OurValuesChooserBlock(StructBlock):
    ourvalues = SnippetChooserBlock(Values)

    class Meta():
        icon = 'fa-anchor'


class OurValuesChooserStreamBlock(StreamBlock):
    item = OurValuesChooserBlock()
    required = False


class WorkForUsPage(TypesetBodyMixin, HeroMixin, Page):
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
    values_text = models.TextField(
        blank=True,
        max_length=255,
        verbose_name='Brief text for values section',
    )
    ourvalues = StreamField(
        OurValuesChooserStreamBlock,
        verbose_name="Our Values Chooser",
        null=True,
        blank=True
    )
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
        FieldPanel('recruitment_policy'),
        FieldPanel('gdr_policy'),
        StreamFieldPanel('benefits'),
        MultiFieldPanel([
            FieldPanel('values_text'),
            StreamFieldPanel('ourvalues')
        ], heading='Our Values'),
        StreamFieldPanel('team_story'),
        FieldPanel('vacancy_title'),
        FieldPanel('vacancy_subtitle_text')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['vacancies'] = VacancyPage.objects.live()
        return context
