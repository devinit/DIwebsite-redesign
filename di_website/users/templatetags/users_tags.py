"""
    Holds the custom template tags relating to the users module
"""

from django import template

from di_website.users.models import UserProfile

register = template.Library()


@register.simple_tag(takes_context=False)
def get_user_profiles():
    profiles = UserProfile.objects.filter(active=True)
    return profiles
