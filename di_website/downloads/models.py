from django import forms
from django.db import models
from django.utils.text import slugify
from django.utils.functional import cached_property
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from .fields import download_streamfield, download_image_streamfield, download_date_streamfield
from .mixins import DownloadGroupMixin
from wagtail.search import index


class SimpleTaxonomy(models.Model):

    class Meta:
        abstract = True
        ordering = ['title']

    title = models.CharField(
        max_length=100,
        help_text='The title of the category'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='The slug must be unqiue for this category'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('slug'),
            ],
            heading='Title and slug',
        ),
    ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(SimpleTaxonomy, self).save(*args, **kwargs)


@register_snippet
class Language(SimpleTaxonomy):
    class Meta:
        verbose_name = 'Language'


class BaseDownload(models.Model):

    class Meta:
        abstract = True

    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
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


@register_snippet
class PublicationDownload(index.Indexed, BaseDownload):

    language = models.ForeignKey(
        'Language',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title'),
        FieldPanel('language', widget=forms.RadioSelect),
    ]

    search_fields = [
        index.SearchField('title', partial_match=True),
    ]

    def __str__(self):
        title = self.title if self.title else self.file.title
        if self.language:
            title = '%s | %s' % (title, self.language.title)
        return title


@register_snippet
class DataDownload(index.Indexed, BaseDownload):

    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title'),
    ]

    search_fields = [
        index.SearchField('title', partial_match=True),
    ]



class DownloadItem(models.Model):

    class Meta:
        abstract = True

    download = models.ForeignKey(
        'downloads.PublicationDownload',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        SnippetChooserPanel('download'),
    ]


class DataDownloadItem(models.Model):

    class Meta:
        abstract = True

    download = models.ForeignKey(
        'downloads.DataDownload',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        SnippetChooserPanel('download'),
    ]


class DownloadDatedItem(models.Model):

    class Meta:
        abstract = True

    date = models.DateTimeField(
        help_text='This date will be used for display and ordering',
    )
    download = models.ForeignKey(
        'Download',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('date'),
        SnippetChooserPanel('download'),
    ]


class DownloadGroupItem(DownloadGroupMixin, models.Model):

    class Meta:
        abstract = True

    downloads = download_streamfield


class DownloadImageGroupItem(DownloadGroupMixin, models.Model):

    class Meta:
        abstract = True

    downloads = download_image_streamfield


class DownloadDatedGroupItem(DownloadGroupMixin, models.Model):

    class Meta:
        abstract = True

    downloads = download_date_streamfield
