from django.db import models

from wagtailmetadata.models import MetadataPageMixin

from wagtail.core.models import Page


class OrganisationDashboard(MetadataPageMixin, Page):
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Organisation Dashboard'

    parent_page_type = ['home.HomePage']
    subpage_types = []
    max_count = 1
