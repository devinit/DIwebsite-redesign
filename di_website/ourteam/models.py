from django.db import models
from django.contrib.auth.models import User

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin
from di_website.users.models import Department, JobTitle

from wagtailmetadata.models import MetadataPageMixin


class TeamMemberMetadataPageMixin(MetadataPageMixin):

    class Meta:
        abstract = True

    def get_meta_image(self):
        if getattr(self.specific, 'search_image', None):
            return self.specific.search_image
        elif getattr(self.specific, 'image', None):
            return self.specific.image
        return super(TeamMemberMetadataPageMixin, self).get_meta_image()

    def get_meta_description(self):
        return self.search_description if self.search_description else self.title

    def get_meta_title(self):
        return self.title


class OurTeamPage(HeroMixin, Page):

    """ List of Team Members Page """

    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    def get_context(self, request):
        context = super(OurTeamPage, self).get_context(request)
        team_filter = request.GET.get('team-filter', None)
        if team_filter:
            context['profiles'] = TeamMemberPage.objects.live().filter(teammember_departments__department__slug=team_filter).order_by('name')
        else:
            context['profiles'] = TeamMemberPage.objects.live().order_by('name')
        context['departments'] = Department.objects.all()
        context['selected_team'] = team_filter

        return context

    class Meta:
        verbose_name = "Our Team Page"

    subpage_types = ['TeamMemberPage', 'general.General']
    parent_page_types = ['about.WhoWeArePage']

    content_panels = Page.content_panels + [
        hero_panels(),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')
    ]


class TeamMemberPage(TeamMemberMetadataPageMixin, Page):
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

    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
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
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    class Meta:
        verbose_name = "Team Member Page"

    subpage_types = ['general.General']
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
