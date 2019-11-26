from django.db import models
from django.utils.text import slugify

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


@register_snippet
class JobTitle(index.Indexed, models.Model):
    name = models.CharField(max_length=255, unique=True)

    search_fields = [
        index.SearchField('name', partial_match=True)
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'


@register_snippet
class Department(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, help_text="Optional. Will be auto-generated from name if left blank.")

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)
