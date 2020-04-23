from django.db import models

from modelcluster.models import ClusterableModel

from wagtail.search import index

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel


@register_snippet
class SpotlightSource(index.Indexed, ClusterableModel):
    name = models.TextField()

    panels = [FieldPanel('name')]

    search_fields = [index.SearchField('name')]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spotlight Source"
        verbose_name_plural = "Spotlight Sources"


@register_snippet
class SpotlightColour(ClusterableModel):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=7)

    panels = [
        FieldPanel('name'),
        FieldPanel('code')
    ]

    def __str__(self):
        return self.name + ' - ' + self.code

    class Meta:
        verbose_name = "Spotlight Colour"
        verbose_name_plural = "Spotlight Colours"
