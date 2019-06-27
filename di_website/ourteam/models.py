from django.shortcuts import render
from wagtail.core.models import Page

from di_website.users.models import UserProfile


class OurTeam(Page):

    """ List of Team Members Page """

    template = "ourteam/ourteam.html"

    def serve(self, request):
        profiles = UserProfile.objects.filter(active=True)
        return render(request, self.template, {
            'page': self,
            'profiles': profiles,
        })

    class Meta:
        verbose_name = "Our Team"
