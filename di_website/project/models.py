from django.db import models

from wagtail.admin.edit_handlers import (StreamFieldPanel)
from wagtail.core.fields import StreamField

from di_website.common.base import StandardPage
from di_website.common.blocks import BaseStreamBlock

class ProjectPage(StandardPage):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    content_panels = StandardPage.content_panels + [
        StreamFieldPanel('body'),
    ]
