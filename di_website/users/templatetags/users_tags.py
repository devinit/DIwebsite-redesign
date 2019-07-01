"""
    Holds the custom template tags relating to the users module
"""

from django import template

from di_website.users.models import UserProfile, Department

register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_profiles(context):
    departments = Department.objects.all()
    team_filter = context['request'].GET.get('team-filter', None)
    if team_filter:
        profiles = UserProfile.objects.filter(active=True, department__slug=team_filter)
    else:
        profiles = UserProfile.objects.filter(active=True)
    return {
        "profiles": profiles,
        "departments": departments,
        "selected_team": team_filter,
    }
