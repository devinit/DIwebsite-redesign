from django.contrib.postgres.fields import JSONField
from django.db import models
from django.http import Http404, JsonResponse

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.edit_handlers import ImageChooserPanel

from di_website.common.constants import MINIMAL_RICHTEXT_FEATURES
from di_website.publications.utils import WagtailImageField


class VisualisationsPage(Page):
    """
    Parent page for all visualisations
    """
    parent_page_types = ['home.HomePage']
    subpage_types = ['visualisation.ChartPage']
    max_count = 1

    class Meta:
        verbose_name = 'Visualisations Page'

    def get_sitemap_urls(self, request):
        return []

    def serve(self, request, *args, **kwargs):
        raise Http404()

    def serve_preview(self, request, mode_name):
        raise Http404()


class ChartPage(RoutablePageMixin, Page):
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
        ImageChooserPanel('fallback_image'),
        MultiFieldPanel([
            FieldPanel('selectable'),
            FieldPanel('aggregated'),
        ], heading='Chart options'),
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
