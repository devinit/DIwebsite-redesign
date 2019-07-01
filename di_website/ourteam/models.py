from django.shortcuts import render
from wagtail.core.models import Page

from di_website.users.models import UserProfile


class OurTeam(Page):

    """ List of Team Members Page """

    class Meta:
        verbose_name = "Our Team"
