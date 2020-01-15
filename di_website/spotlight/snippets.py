from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.search import index

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel


@register_snippet
class Source(index.Indexed, ClusterableModel):
    name = models.TextField()

    panels = [FieldPanel('name')]

    search_fields = [index.SearchField('name')]


@register_snippet
class Colour(ClusterableModel):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=7)

    panels = [
        FieldPanel('name'),
        FieldPanel('code')
    ]
