from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Orderable


class AbstractLink(models.Model):
    class Meta:
        abstract = True

    label = models.CharField(max_length=255)
    hidden = models.BooleanField(default=False)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )
    panels = [
        FieldPanel('label'),
        FieldPanel('hidden'),
        PageChooserPanel('page'),
    ]


class PrimaryMenuLinks(Orderable, AbstractLink):
    item = ParentalKey('PrimaryMenu', related_name='primary_menu_links')


@register_setting
class PrimaryMenu(ClusterableModel, BaseSetting):

    panels = [
        MultiFieldPanel(
            [
                InlinePanel('primary_menu_links', label='Primary menu link'),
            ],
            heading='Primary menu',
        ),
    ]
