from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from di_website.common.base import StandardPage
from di_website.users.models import UserProfile


class OurTeamPage(StandardPage):

    """ List of Team Members Page """

    class Meta:
        verbose_name = "Our Team Page"


class TeamMemberPage(Page):
    """Individual team member page. Autocreated when profile is."""
    user_profile = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )

    class Meta:
        verbose_name = "Team Member Page"

    content_panels = Page.content_panels + [
        FieldPanel('user_profile')
    ]

    parent_page_types = [
        'OurTeamPage'
    ]
