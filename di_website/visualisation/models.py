from django.contrib.postgres.fields import JSONField
from django.db import models
from django.http import Http404, JsonResponse
from django.utils.functional import cached_property

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from di_website.common.edit_handlers import HelpPanel
from di_website.common.constants import INSTRUCTIONS_RICHTEXT_FEATURES, MINIMAL_RICHTEXT_FEATURES, SIMPLE_RICHTEXT_FEATURES
from di_website.visualisation.mixins import (
    InstructionsMixin, GeneralInstructionsMixin, SpecificInstructionsMixin,
    ChartOptionsMixin, PlotlyOptionsMixin, D3OptionsMixin, FallbackImageMixin, EChartOptionsMixin
)
from di_website.visualisation.utils import (
    ChartOptionsPanel, InstructionsPanel, SpecificInstructionsPanel,
    PlotlyOptionsPanel, D3OptionsPanel, FallbackImagePanel, EChartOptionsPanel
)
from di_website.visualisation.fields import AceEditorField


class VisualisationsPage(GeneralInstructionsMixin, Page):
    """
    Parent page for all visualisations
    """
    parent_page_types = ['home.HomePage']
    subpage_types = ['visualisation.ChartPage', 'visualisation.AdvancedChartPage']
    max_count = 1

    class Meta:
        verbose_name = 'Visualisations Page'

    no_js_text = models.CharField(
        max_length=255,
        default='To view this interactive visualisation make sure JavaScript is available on your device.',
        help_text='Text that is displayed for all charts when the user does not have JavaScript available',
    )

    larger_screen_text = models.CharField(
        max_length=255,
        default='To view this interactive visualisation use a device with a larger screen.',
        help_text='Text that is displayed for individual charts when the user\'s screen is less than the minimum width defined in the chart page',
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                HelpPanel('''
                    Fallback text displayed for charts when JavaScript is unavailable or screen size is less than the defined minimum width.
                ''', wrapper_class='help-block help-info no-padding-top'),
                FieldPanel('no_js_text'),
                FieldPanel('larger_screen_text'),
            ],
            heading='Fallback text',
        ),
        MultiFieldPanel(
            [
                HelpPanel('''
                    Optional: a general set of instructions that can be selected to display with child visualisation content.
                ''', wrapper_class='help-block help-info no-padding-top'),
                FieldPanel('instructions'),
            ],
            heading='Interactive visualisation instructions',
        ),
    ]

    def get_sitemap_urls(self, request):
        return []

    def serve(self, request, *args, **kwargs):
        raise Http404()

    def serve_preview(self, request, mode_name):
        raise Http404()


class ChartPage(ChartOptionsMixin, SpecificInstructionsMixin, FallbackImageMixin, RoutablePageMixin, Page):
    """
    Individual chart page
    """
    parent_page_types = [VisualisationsPage]
    subpage_types = []

    class Meta:
        verbose_name = 'Plotly Studio Chart Page'

    subtitle = models.TextField(
        blank=True,
        null=True,
        help_text="Optional: subtitle to appear underneath the chart title."
    )

    chart_json = JSONField(
        verbose_name="Chart JSON",
        help_text='Paste exported Chart Studio JSON here. To preserve data integretity, the JSON data should not be edited in Wagtail'
    )
    caption = RichTextField(
        null=True,
        blank=True,
        help_text='Optional: caption text and link(s) for the chart',
        features=MINIMAL_RICHTEXT_FEATURES
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('chart_json'),
        FallbackImagePanel(),
        ChartOptionsPanel(),
        SpecificInstructionsPanel(),
        FieldPanel('caption')
    ]

    @cached_property
    def parent(self):
        return self.get_parent().specific

    @cached_property
    def instructions_text(self):
        if self.instructions:
            return self.instructions

        elif self.display_general_instructions and self.parent.instructions:
            return self.parent.instructions

        return ''

    def get_sitemap_urls(self, request):
        return []

    @route(r'^$')
    def chart(self, request):
        if request.user.is_authenticated:
            return super().serve(request)
        raise Http404()

    @route(r'^data/$')
    def data(self, request):
        return JsonResponse(self.chart_json)


class AdvancedChartPage(InstructionsMixin, EChartOptionsMixin, D3OptionsMixin, PlotlyOptionsMixin, FallbackImageMixin, RoutablePageMixin, Page):
    """
    A code based chart page for advanced users
    """
    parent_page_types = [VisualisationsPage]
    subpage_types = []

    subtitle = models.TextField(
        blank=True,
        null=True,
        help_text="Optional: subtitle to appear underneath the chart title."
    )

    html = AceEditorField(options={'mode':'html'}, blank=True, default='{% load wagtailcore_tags %}')
    javascript = AceEditorField(options={'mode':'javascript'}, blank=True, default='"use strict";')
    css = AceEditorField(options={'mode':'css'}, blank=True, default='/* CSS goes here */')

    caption = RichTextField(
        null=True,
        blank=True,
        help_text='Optional: caption text and link(s) for the chart',
        features=INSTRUCTIONS_RICHTEXT_FEATURES + SIMPLE_RICHTEXT_FEATURES
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        PlotlyOptionsPanel(),
        D3OptionsPanel(),
        EChartOptionsPanel(),
        FieldPanel('html', classname='collapsible'),
        FieldPanel('javascript', classname='collapsible'),
        # FieldPanel('css', classname='collapsible'), TODO: add CSS support - may work best in an iFrame
        FallbackImagePanel(),
        InstructionsPanel(),
        FieldPanel('caption'),
    ]

    @cached_property
    def parent(self):
        return self.get_parent().specific

    @cached_property
    def instructions_text(self):
        if self.instructions:
            return self.instructions

        return ''

    def get_sitemap_urls(self, request):
        return []

    @route(r'^$')
    def chart(self, request):
        if request.user.is_authenticated:
            return super().serve(request)
        raise Http404()

    class Meta:
        verbose_name = 'Advanced Chart Page'
