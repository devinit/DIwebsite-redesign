from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    FieldPanel,
)


@register_snippet
class JobTitle(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'


@register_snippet
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, help_text="Optional. Will be auto-generated from name if left blank.")

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)
