from django import template
from di_website.publications.models import PodcastProvider

register = template.Library()

@register.inclusion_tag('publications/tags/podcast_platforms.html', takes_context=True)
def podcast_platforms(context):
    return {
        'podcast_platforms': PodcastProvider.objects.all(),
        'request': context['request'],
    }
