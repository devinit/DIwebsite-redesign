from django.db import models

# Create your models here.
from wagtail.core.models import Page

from wagtail.admin.edit_handlers import  StreamFieldPanel
from wagtail.core.fields import StreamField
from di_website.streams import blocks

class OurTeam(Page):
    
    """ List of Team Members Page """

    template = "ourteam/ourteam.html"

    team = StreamField(
        [
            ("profiles",blocks.TeamProfileBlock())
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("team"),
    ]

    class Meta:
        verbose_name = "Our Team"