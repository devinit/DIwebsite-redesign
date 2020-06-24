import json
from django.db import models
from django.http import Http404, JsonResponse

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from .fields import AceEditorField


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
    parent_page_types = [VisualisationsPage]
    subpage_types = []

    chart_json = AceEditorField(blank=True, default='{ "data":[], "layout":{} }', verbose_name="Chart JSON")

    content_panels = Page.content_panels + [
        FieldPanel('chart_json')
    ]

    class Meta:
        verbose_name = 'Chart Page'

    def get_sitemap_urls(self, request):
        return []

    @route(r'^$')
    def chart(self, request):
        if request.user.is_authenticated:
            return super().serve(request)
        raise Http404()

    @route(r'^data/$')
    def data(self, request):
        return JsonResponse(json.loads(self.chart_json))
