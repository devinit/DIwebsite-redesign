from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from di_website.common.base import StandardPage
from di_website.users.models import Department, JobTitle
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from django.contrib.auth.models import User
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField


class OurTeamPage(StandardPage):

    """ List of Team Members Page """

    def get_context(self, request):
        context = super(OurTeamPage, self).get_context(request)
        team_filter = request.GET.get('team-filter', None)
        if team_filter:
            context['profiles'] = TeamMemberPage.objects.live().filter(department__slug=team_filter)
        else:
            context['profiles'] = TeamMemberPage.objects.live()
        context['departments'] = Department.objects.all()
        context['selected_team'] = team_filter

        return context

    class Meta:
        verbose_name = "Our Team Page"

    subpage_types = ['TeamMemberPage']


class TeamMemberPage(Page):
    """Individual team member page. Autocreated when profile is."""
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    position = models.ForeignKey(
        JobTitle,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    telephone = models.CharField(max_length=255, null=True, blank=True)
    my_story=RichTextField(blank=True,null=True,help_text="Please say something about team member ")

    content_panels = Page.content_panels + [
        FieldPanel('user'),
        FieldPanel('name'),
        ImageChooserPanel('image'),
        SnippetChooserPanel('position'),
        SnippetChooserPanel('department'),
        FieldPanel('email'),
        FieldPanel('telephone'),
        FieldPanel('my_story', classname="full"),
    ]

    class Meta:
        verbose_name = "Team Member Page"

    parent_page_types = [
        'OurTeamPage'
    ]
