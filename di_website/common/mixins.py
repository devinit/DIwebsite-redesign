from django.db import models
from django.utils.functional import cached_property

from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey

from .blocks import BaseStreamBlock, SectionStreamBlock, TypesetStreamBlock


class HeroMixin(models.Model):
    class Meta:
        abstract = True

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Hero Image'
    )
    hero_image_credit_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Image credit name',
        help_text='Name of source of image used in hero if any'
    )
    hero_image_credit_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image credit url',
        help_text='A Link to the original source of the image if any'
    )
    hero_text = RichTextField(
        null=True,
        blank=True,
        help_text='A description of the page content'
    )
    hero_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero link',
        help_text='Choose a page to link to for the Call to Action'
    )
    hero_link_caption = models.CharField(
        max_length=255,
        blank=True,
        help_text='Text to display on the link button'
    )


class OtherPageMixin(Orderable):
    other_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Page',
        help_text='A page to link to in the "Other Pages or Related Links" section'
    )

    class Meta():
        abstract = True


class BaseStreamBodyMixin(models.Model):
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class TypesetBodyMixin(models.Model):
    body = StreamField(
        TypesetStreamBlock(),
        verbose_name="Page Body",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class SectionBodyMixin(models.Model):
    sections = StreamField(
        SectionStreamBlock(),
        verbose_name="Sections",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class BaseDownloadMixin(models.Model):
    class Meta:
        abstract = True

    page = ParentalKey(
        Page, related_name='page_downloads', on_delete=models.CASCADE
    )
    file = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional: document title, defaults to the file name if left blank',
    )

    @cached_property
    def get_title(self):
        return self.title if self.title else self.file.title

    def __str__(self):
        return self.title if self.title else self.file.title

class TeamMemberStoryMixin(models.Model):

    team_member_quote = models.TextField(
        null=True, 
        blank=True,
        verbose_name='Quote from team member')

    quote_owner = models.ForeignKey('ourteam.TeamMemberPage',        
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+' )


    team_page = models.ForeignKey(
        'ourteam.OurTeamPage',        
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+' )
    
    team_stories = models.ForeignKey(
        'blog.BlogIndexPage',        
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+' )

    class Meta:
        abstract=True
