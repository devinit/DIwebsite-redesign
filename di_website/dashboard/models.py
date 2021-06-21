from django.db import models
from django.utils.functional import cached_property

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

    @cached_property
    def get_sections(self):
        sections = [
            # { 'id': 'summary', 'caption': 'Summary' },
            { 'id': 'finance', 'caption': 'Finance' },
            { 'id': 'development', 'caption': 'Development & Fundraising' },
            { 'id': 'it', 'caption': 'IT' },
            { 'id': 'hr', 'caption': 'Human Resources' },
            { 'id': 'project-management', 'caption': 'Project Management' },
            { 'id': 'communications', 'caption': 'Communications' },
        ]

        return sections
