from django.shortcuts import render

from di_website.common.base import StandardPage

class OurTeam(StandardPage):

    """ List of Team Members Page """

    class Meta:
        verbose_name = "Our Team"
