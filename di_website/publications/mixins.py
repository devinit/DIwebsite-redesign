from django.db import models
from .fields import flexible_content_streamfield, content_streamfield


class FlexibleContentMixin(models.Model):
    class Meta:
        abstract = True

    content = flexible_content_streamfield()


class ContentMixin(models.Model):
    class Meta:
        abstract = True

    content = content_streamfield()


class OptionalContentMixin(models.Model):
    class Meta:
        abstract = True

    content = content_streamfield(blank=True)
