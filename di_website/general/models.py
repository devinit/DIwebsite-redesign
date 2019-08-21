from django.db import models
from di_website.common.blocks import DocumentBoxSectionBlock, DuoContentStreamBlock
from di_website.common.mixins import (
    TeamMemberStoryMixin,
    HeroMixin,
    BaseStreamBodyMixin
)

from di_website.common.base import team_member_story_panels, hero_panels

from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel
)

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    InlinePanel,
)

from wagtail.core.fields import StreamField
from wagtail.core.models import Page


class General(HeroMixin, TeamMemberStoryMixin, BaseStreamBodyMixin, Page):

    """
    General page that that can be used with strategy  and accounts pages
    """

    template = 'general/general_page.html'

    downloads = StreamField([
        ('downloads', DocumentBoxSectionBlock()), ], verbose_name="Downloads Section",)

    content = StreamField(DuoContentStreamBlock(), blank=True)
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='More about'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        team_member_story_panels(),
        StreamFieldPanel('content'),
        StreamFieldPanel('downloads'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related pages')
        ], heading='Other Pages/Related Links'),
    ]

    class Meta:
        verbose_name = 'General Page'
