from django.db import models
from wagtail.fields import StreamField

from .blocks import FeaturedContentBlock, FeaturedWorkBlock
from di_website.common.blocks import SectionStreamBlock


class HomePageContentMixin(models.Model):
    class Meta:
        abstract = True

    content = StreamField([('featured_content', FeaturedContentBlock()),
                          ('sections', SectionStreamBlock(required=False, verbose_name="Sections")),
                          ('featured_work', FeaturedWorkBlock())],
                          blank=True,
                          use_json_field=True)
