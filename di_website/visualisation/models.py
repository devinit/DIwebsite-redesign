from django.contrib.postgres.fields import JSONField
from django.db import models
from django.http import Http404, JsonResponse
from django.utils.functional import cached_property

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.edit_handlers import ImageChooserPanel

from di_website.common.edit_handlers import HelpPanel
from di_website.common.constants import MINIMAL_RICHTEXT_FEATURES
from di_website.publications.utils import WagtailImageField
from di_website.visualisation.mixins import GeneralInstructionsMixin, SpecificInstructionsMixin


class VisualisationsPage(GeneralInstructionsMixin, Page):
    """
    Parent page for all visualisations
    """
    parent_page_types = ['home.HomePage']
    subpage_types = ['visualisation.ChartPage']
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


class ChartPage(SpecificInstructionsMixin, RoutablePageMixin, Page):
    """
    Individual chart page
    """
    parent_page_types = [VisualisationsPage]
    subpage_types = []

    class Meta:
        verbose_name = 'Chart Page'

    chart_json = JSONField(
        verbose_name="Chart JSON",
        help_text='Paste exported Chart Studio JSON here. To preserve data integretity, the JSON data should not be edited in Wagtail'
    )
    fallback_image = WagtailImageField(
        required=True,
        help_text='Fallback image for the chart',
    )
    display_fallback_mobile = models.BooleanField(
        default=True,
        help_text='Optional: when selected devices with screen widths up to 400px will be served the fallback image',
        verbose_name='Show on mobile'
    )
    display_fallback_tablet = models.BooleanField(
        default=False,
        help_text='Optional: when selected devices with screen widths up to 700px will be served the fallback image',
        verbose_name='Show on tablet'
    )
    selectable = models.BooleanField(
        default=False,
        help_text='Optional: selectable charts individusalise the data display a dropdown to select data'
    )
    aggregated = models.BooleanField(
        default=False,
        help_text='Optional: aggregated charts adds an "All data" option to selectable charts'
    )
    selector_includes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to include in the dropdown selector. Use when inclusions are fewer than exclusions'
    )
    selector_excludes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to exclude in the dropdown selector. Use when exclusions are fewer than inclusions'
    )
    aggregation_includes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to include in the aggregated chart. Use when inclusions are fewer than exclusions'
    )
    aggregation_excludes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to exclude in the aggregated chart. Use when exclusions are fewer than inclusions'
    )
    aggregate_option_label = models.CharField(
        null=True, blank=True, default='All data', max_length=255,
        help_text='The label of the "All data" option on aggregated charts'
    )
    caption = RichTextField(
        null=True,
        blank=True,
        help_text='Optional: caption text and link(s) for the chart',
        features=MINIMAL_RICHTEXT_FEATURES
    )

    content_panels = Page.content_panels + [
        FieldPanel('chart_json'),
        MultiFieldPanel([
            ImageChooserPanel('fallback_image'),
            FieldPanel('display_fallback_mobile'),
            FieldPanel('display_fallback_tablet'),
        ], heading='Fallback image and options'),
        MultiFieldPanel([
            FieldPanel('selectable'),
            FieldPanel('selector_includes'),
            FieldPanel('selector_excludes'),
            FieldPanel('aggregated'),
            FieldPanel('aggregation_includes', classname='full'),
            FieldPanel('aggregation_excludes', classname='full'),
            FieldPanel('aggregate_option_label', classname='full full-custom')
        ], heading='Chart options'),
        MultiFieldPanel(
            [
                HelpPanel('''
                    Optional: if the checkbox is selected, the general instructions from the parent page will be displayed.<br>
                    Specific instuctions added to this page will be displayed, overriding this setting.
                ''', wrapper_class='help-block help-info no-padding-top'),
                FieldPanel('display_general_instructions'),
                FieldPanel('instructions'),
            ],
            heading='Interactive visualisation instructions',
        ),
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
