from django.db import models
from django.shortcuts import render
from django.utils.text import slugify
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.models import Page
from di_website.common.base import StandardPage
from di_website.users.models import Department,JobTitle
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from django.contrib.auth.models import User
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.routable_page.models import RoutablePageMixin, route

class OurTeamIndexPage(RoutablePageMixin,StandardPage):

    """ List of Team Members Page """
    template="ourteam/our_team_page.html"

    def get_context(self, request):
        context = super(OurTeamIndexPage, self).get_context(request)
        context['profiles'] = TeamMemberPage.objects.live()
        context['departments'] = Department.objects.all()

        return context

    @route(r"(team-filter=\w+)$", name='team_filter')
    def team_filter(self, request, filter_query=None):
        department = Department.objects.get(slug=filter_query)
        profiles = TeamMemberPage.object.get(department_id = department.id)
        context = super(OurTeamIndexPage, self).get_context(request)
        context['profiles'] = profiles
        context['departments'] = Department.objects.all()

        return render(request, self.template, context)

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
    active = models.BooleanField(default=False, help_text="Should this user's profile be displayed as staff?")

    content_panels = [
        FieldPanel('user'),
        FieldPanel('name'),
        ImageChooserPanel('image'),
        SnippetChooserPanel('position'),
        SnippetChooserPanel('department'),
        FieldPanel('email'),
        FieldPanel('telephone'),
        FieldPanel('active')
    ]

    def clean(self):
        super().clean()
        self.title = self.name
        self.slug = slugify(self.name) 

    def __str__(self):
        return "{} ({})".format(self.name if self.name else self.user.username, "Active" if self.active else "Inactive")

    
    class Meta:
        verbose_name = "Team Member Page"
    

    parent_page_types = [
        'OurTeamIndexPage'
    ]

TeamMemberPage._meta.get_field('slug').default = 'default-blank-slug'