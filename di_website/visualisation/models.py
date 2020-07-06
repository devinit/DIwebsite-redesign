from django.contrib.postgres.fields import JSONField
from django.db import models
from django.http import Http404, JsonResponse

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

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('instructions'),
                HelpPanel('''
                    Optional: a general set of instructions that can be selected to display with child visualisation content.
                ''', wrapper_class='help-block help-info'),
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
        help_text='Optional: when selected devices with screen widths up to 400px will be served the fallback image'
    )
    display_fallback_tablet = models.BooleanField(
        default=False,
        help_text='Optional: when selected devices with screen widths up to 700px will be served the fallback image'
    )
    selectable = models.BooleanField(
        default=False,
        help_text='Optional: selectable charts individusalise the data display a dropdown to select data'
    )
    aggregated = models.BooleanField(
        default=False,
        help_text='Optional: aggregated charts adds an "All data" option to selectable charts'
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
            FieldPanel('fallback_image'),
            FieldPanel('display_fallback_mobile'),
            FieldPanel('display_fallback_tablet'),
        ], heading='Fallback image and options'),
        ImageChooserPanel('fallback_image'),
        MultiFieldPanel([
            FieldPanel('selectable'),
            FieldPanel('aggregated'),
        ], heading='Chart options'),
        MultiFieldPanel(
            [
                FieldPanel('display_general_instructions'),
                FieldPanel('instructions'),
                HelpPanel('''
                    Optional: if the checkbox is selected, the general instructions from the parent page will be displayed.<br>
                    Specific instuctions added to this page will be displayed, overriding this setting.
                ''', wrapper_class='help-block help-info'),
            ],
            heading='Interactive visualisation instructions',
        ),
        FieldPanel('caption')
    ]

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
