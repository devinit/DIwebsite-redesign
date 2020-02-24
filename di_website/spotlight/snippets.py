from django.db import models
from django.utils.text import slugify

from modelcluster.models import ClusterableModel

from wagtail.search import index

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel


@register_snippet
class Spotlight(ClusterableModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Spotlight"
        verbose_name_plural = "Spotlights"

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Spotlight, self).save(**kwargs)


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
