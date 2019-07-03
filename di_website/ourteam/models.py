from django.shortcuts import render
from wagtail.core.models import Page

from di_website.users.models import UserProfile
from di_website.common.base import StandardPage

class OurTeam(StandardPage):

    """ List of Team Members Page """

    class Meta:
        verbose_name = "Our Team"
