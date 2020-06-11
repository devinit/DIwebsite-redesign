from django.db import models
from django.shortcuts import redirect

from wagtail.core.models import Page


class VisualisationsPage(Page):
    """
    Parent page for all visualisations
    """
    parent_page_types = ['home.HomePage']
    subpage_types = ['visualisation.ChartPage']

    class Meta:
        verbose_name = 'Visualisations Page'

    def get_sitemap_urls(self, request):
        return []

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_parent().url)

    def serve_preview(self, request, mode_name):
        return self.get_parent().serve(request)


class ChartPage(Page):
    parent_page_types = [VisualisationsPage]
    subpage_types = []

    class Meta:
        verbose_name = 'Chart Page'

    def get_sitemap_urls(self, request):
        return []

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_parent().url)

    def serve_preview(self, request, mode_name):
        return self.get_parent().serve(request)
