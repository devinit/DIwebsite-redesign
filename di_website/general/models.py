from django.db import models
from di_website.home.models import StandardPage
from di_website.ourteam.models import TeamMemberPage, OurTeamPage
from di_website.blog.models import BlogIndexPage

from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel
)

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel
)

# Create your models here.
class Strategy(StandardPage):


    template = 'general/general_page.html'

    team_member_quote = models.TextField(
        null=True, 
        blank=False,
        verbose_name='Quote from team member')

    quote_owner = models.ForeignKey(TeamMemberPage,        
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+' )


    team_page = models.ForeignKey(
        OurTeamPage,        
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+' )
    
    team_stories = models.ForeignKey(
        BlogIndexPage,        
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+' )

    content_panels = StandardPage.content_panels + [
        MultiFieldPanel([
            FieldPanel('team_member_quote'),
            PageChooserPanel('quote_owner','ourteam.TeamMemberPage'),
            PageChooserPanel('team_page','ourteam.OurTeamPage'),
            PageChooserPanel('team_stories','blog.BlogIndexPage')
        ],heading='Team member quote',classname="collapsible collapsed")
    ]