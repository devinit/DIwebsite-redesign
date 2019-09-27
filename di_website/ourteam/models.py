from django.db import models
from django.contrib.auth.models import User

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin
from di_website.users.models import Department, JobTitle


class OurTeamPage(HeroMixin, Page):

    """ List of Team Members Page """

    def get_context(self, request):
        context = super(OurTeamPage, self).get_context(request)
        team_filter = request.GET.get('team-filter', None)
        if team_filter:
            context['profiles'] = TeamMemberPage.objects.live().filter(teammember_departments__department__slug=team_filter)
        else:
            context['profiles'] = TeamMemberPage.objects.live()
        context['departments'] = Department.objects.all()
        context['selected_team'] = team_filter

        return context

    class Meta:
        verbose_name = "Our Team Page"

    subpage_types = ['TeamMemberPage']
    parent_page_types = ['about.WhoWeArePage']

    content_panels = Page.content_panels + [
        hero_panels(),
        InlinePanel('page_notifications', label='Notifications')
    ]


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
    email = models.EmailField(
        null=True,
        blank=True
    )
    telephone = models.CharField(max_length=255, null=True, blank=True)
    my_story = RichTextField(
        blank=True,
        null=True,
        help_text="Please say something about team member"
    )

    content_panels = Page.content_panels + [
        FieldPanel('user'),
        FieldPanel('name'),
        ImageChooserPanel('image'),
        SnippetChooserPanel('position'),
        InlinePanel('teammember_departments', label="Departments"),
        FieldPanel('email'),
        FieldPanel('telephone'),
        FieldPanel('my_story', classname="full"),
        InlinePanel('page_notifications', label='Notifications')
    ]

    class Meta:
        verbose_name = "Team Member Page"

    parent_page_types = [
        'OurTeamPage'
    ]


class TeamMemberPageDepartment(Orderable, models.Model):
    page = ParentalKey('ourteam.TeamMemberPage', on_delete=models.CASCADE, related_name='teammember_departments')
    department = models.ForeignKey('users.Department', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "team member department"
        verbose_name_plural = "team member departments"

    panels = [
        SnippetChooserPanel('department'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.department.name
