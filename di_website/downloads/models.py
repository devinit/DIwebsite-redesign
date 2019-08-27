from django import forms
from django.db import models
from django.utils.functional import cached_property
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from .fields import download_streamfield, download_image_streamfield, download_date_streamfield
from .mixins import DownloadGroupMixin


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
class Download(BaseDownload):

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

    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title'),
        FieldPanel('language', widget=forms.RadioSelect),
    ]

    def __str__(self):
        title = self.title if self.title else self.file.title
        if self.language:
            title = '%s | %s' % (title, self.language.title)
        return title


@register_snippet
class DataDownload(BaseDownload):

    panels = [
        DocumentChooserPanel('file'),
        FieldPanel('title'),
    ]


class DownloadItem(models.Model):

    class Meta:
        abstract = True

    download = models.ForeignKey(
        'Download',
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
        'DataDownload',
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
