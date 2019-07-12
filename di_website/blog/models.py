from django.db import models
from di_website.common.base import StandardPage
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


@register_snippet
class BlogTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class BlogIndexPage(StandardPage):
    subpage_types = ['BlogArticlePage']


class BlogArticlePage(StandardPage):
    topic = models.ForeignKey(
        BlogTopic,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = StandardPage.content_panels + [
        SnippetChooserPanel('topic')
    ]

    parent_page_types = [
        'BlogIndexPage'
    ]
