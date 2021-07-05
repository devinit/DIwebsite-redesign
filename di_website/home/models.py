"""
Home page models, reusable snippets, other common models
"""
from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
    StreamFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.snippets.models import register_snippet
from wagtail.core.blocks import CharBlock, PageChooserBlock, RichTextBlock, StructBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtailmetadata.models import MetadataPageMixin

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from di_website.common.base import hero_panels, get_related_pages
from di_website.common.mixins import HeroMixin, OtherPageMixin, SectionBodyMixin, TypesetBodyMixin
from di_website.common.constants import SIMPLE_RICHTEXT_FEATURES, RICHTEXT_FEATURES_NO_FOOTNOTES


class AbstractLink(models.Model):
    """
    Contains common properties for links

    Arguments:
        Model {Django Model}
    """
    class Meta:
        abstract = True

    label = models.CharField(
        max_length=255,
        blank=True
    )
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_url = models.URLField(blank=True)

    panels = [
        FieldPanel('label'),
        PageChooserPanel('page'),
        FieldPanel('link_url')
    ]


@register_snippet
class NewsLetter(models.Model):
    caption = models.CharField(
        max_length=255,
        default='Sign up for our newsletter to receive regular news and updates',
    )
    link_label = models.CharField(
        max_length=255,
        default='Subscribe here'
    )
    link_url = models.URLField(blank=True)

    panels = [
        FieldPanel('caption'),
        FieldPanel('link_label'),
        FieldPanel('link_url')
    ]

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'


@register_snippet
class FooterSection(Orderable, ClusterableModel):
    title = models.CharField(max_length=255)
    show_navigation_links = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        FieldPanel('show_navigation_links'),
        InlinePanel('footer_section_links', label='Section Links'),
        InlinePanel('footer_social_links', label='Social Links')
    ]

    def __str__(self):
        return self.title

    class Meta(Orderable.Meta):
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Sections"


class FooterLink(Orderable, AbstractLink):
    section = ParentalKey(
        'FooterSection', on_delete=models.CASCADE, related_name="footer_section_links")

    def __str__(self):
        return self.page.title if self.page else self.label

    class Meta(Orderable.Meta):
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"


class SocialLink(Orderable, models.Model):
    SOCIAL_CHOICES = [
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('linkedin', 'Linked In'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('flickr', 'Flickr'),
    ]

    social_platform = models.CharField(
        max_length=100,
        choices=SOCIAL_CHOICES
    )
    link_url = models.CharField(max_length=255, default='')
    section = ParentalKey(
        'FooterSection', on_delete=models.CASCADE, related_name="footer_social_links")

    panels = [
        FieldPanel('social_platform'),
        FieldPanel('link_url')
    ]

    def __str__(self):
        return self.social_platform

    class Meta(Orderable.Meta):
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'


@register_snippet
class FooterText(models.Model):
    major_content = RichTextField(features=SIMPLE_RICHTEXT_FEATURES, blank=True)
    body = RichTextField(features=SIMPLE_RICHTEXT_FEATURES)

    panels = [
        FieldPanel('major_content'),
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer Text"

    class Meta:
        verbose_name_plural = 'Footer Text'


@register_snippet
class CookieNotice(models.Model):
    heading = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    download_link_caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='Link Caption')
    cookie_policy = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Policy Doc'
    )

    panels = [
        FieldPanel('heading'),
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('download_link_caption'),
            DocumentChooserPanel('cookie_policy'),
        ], heading='Download Link'),
    ]

    def __str__(self):
        return self.heading or self.body or 'Blank Notice'

    class Meta():
        verbose_name = "Cookie Notice"
        verbose_name_plural = "Cookie Notices"


class HomePageMetaData(MetadataPageMixin):

    class Meta:
        abstract = True

    def get_meta_image(self):
        if getattr(self.specific, 'search_image', None):
            return self.specific.search_image
        elif getattr(self.specific, 'hero_image', None):
            return self.specific.hero_image
        elif getattr(self.specific, 'featured_publication', None) and getattr(self.specific.featured_publication.specific, 'hero_image', None):
            return self.specific.featured_publication.specific.hero_image
        return super(HomePageMetaData, self).get_meta_image()

    def get_meta_description(self):
        return self.search_description if self.search_description else self.title

    def get_meta_title(self):
        return self.title


class HomePage(HomePageMetaData, SectionBodyMixin, Page):
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Home Page'

    parent_page_types = []  # prevent from being a child page

    featured_publication = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The page to showcase in the page hero',
        verbose_name='Featured page'
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Overwrites the hero image of the featured publication'
    )
    hero_link_caption = models.CharField(
        max_length=255,
        blank=True,
        help_text='Text to display on the link button',
        default='View full page'
    )
    featured_content = StreamField([
        ('content', StructBlock([
            ('title', CharBlock()),
            ('body', RichTextBlock(features=RICHTEXT_FEATURES_NO_FOOTNOTES)),
            ('related_page', PageChooserBlock(required=False)),
            ('button_caption', CharBlock(required=False, help_text='Overwrite title text from the related page'))
        ], template='home/blocks/featured_content.html'))
    ], null=True, blank=True)
    featured_work_heading = models.CharField(
        blank=True,
        null=True,
        default='Featured work',
        max_length=200,
        verbose_name='Section heading'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            PageChooserPanel('featured_publication', [
                'publications.PublicationPage',
                'publications.ShortPublicationPage',
                'publications.LegacyPublicationPage',
                'publications.AudioVisualMedia',
                'news.NewsStoryPage',
                'blog.BlogArticlePage',
                'events.EventPage',
                'project.ProjectPage'
            ]),
            ImageChooserPanel('hero_image'),
            FieldPanel('hero_link_caption')
        ], heading='Hero Section'),
        StreamFieldPanel('featured_content'),
        MultiFieldPanel([
            FieldPanel('featured_work_heading'),
            InlinePanel('featured_pages', label='Featured Pages')
        ], heading='Featured Work'),
        StreamFieldPanel('sections'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['featured_pages'] = [link.other_page for link in self.featured_pages.all().order_by('sort_order') if link.other_page.live]

        return context


class HomePageFeaturedWork(OtherPageMixin):
    page = ParentalKey(
        Page, related_name='featured_pages', on_delete=models.CASCADE)

    class Meta:
        ordering = ('sort_order',)

    panels = [
        PageChooserPanel('other_page')
    ]


class StandardPage(SectionBodyMixin, TypesetBodyMixin, HeroMixin, Page):
    """
    A generic content page. It could be used for any type of page content that only needs a hero,
    streamfield content, and related fields
    """
    other_pages_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Heading',
        default='Related content'
    )

    content_panels = Page.content_panels + [
        hero_panels(),
        StreamFieldPanel('body'),
        StreamFieldPanel('sections'),
        MultiFieldPanel([
            FieldPanel('other_pages_heading'),
            InlinePanel('other_pages', label='Related links')
        ], heading='Other Pages/Related Links'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['related_pages'] = get_related_pages(self, self.other_pages.all())

        return context

    class Meta():
        verbose_name = 'Standard Page'


class StandarPageRelatedLink(OtherPageMixin):
    page = ParentalKey(
        Page, related_name='other_pages', on_delete=models.CASCADE)

    panels = [
        PageChooserPanel('other_page')
    ]
