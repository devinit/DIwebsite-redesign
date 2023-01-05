from django.utils.timezone import now
from django.db import models
from django.utils.functional import cached_property
from di_website.common.constants import MAX_RELATED_LINKS

from wagtail.models import Page
from wagtail.contrib.redirects.models import Redirect
from wagtail.search import index

from di_website.common.base import get_related_pages
from di_website.common.templatetags.string_utils import uid

from .fields import flexible_content_streamfield, content_streamfield
from .utils import WagtailImageField, get_downloads


RELATED_CHOICES = (
    ('manual', 'Manual'),
    ('country', 'Country'),
    ('topic', 'Topic')
)


class FilteredDatasetMixin(object):
    @cached_property
    def filtered_datasets(self):
        results = []
        all_pub_datasets = self.publication_datasets.all()
        for pub_dataset in all_pub_datasets:
            if type(pub_dataset.dataset.specific).__name__ == "DatasetPage":
                results.append(pub_dataset)
        return results


class UniquePageMixin(object):
    @classmethod
    def can_create_at(cls, parent) -> bool:
        return super(UniquePageMixin, cls).can_create_at(parent) and not cls.objects.exists()


class UniqueForParentPageMixin(object):
    @classmethod
    def can_create_at(cls, parent) -> bool:
        return super(UniqueForParentPageMixin, cls).can_create_at(parent) \
            and not parent.get_children().type(cls).exists()


class ParentPageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.FilterField('slug')
    ]


class PageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.FilterField('slug'),
        index.SearchField('content', partial_match=True)
    ]


class LegacyPageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.FilterField('slug'),
        index.SearchField('raw_content', partial_match=True),
        index.SearchField('content', partial_match=True)
    ]


class PublicationPageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.FilterField('slug'),
        index.SearchField('title', partial_match=True),
        index.SearchField('hero_text', partial_match=True)
    ]


def CustomPageSearchFields(fields):
    return Page.search_fields + [index.SearchField(x, partial_match=True) for x in fields]


class PublishedDateMixin(models.Model):
    class Meta:
        abstract = True

    published_date = models.DateTimeField(
        blank=True,
        default=now,
        help_text='This date will be used for display and ordering',
    )


class UUIDMixin(models.Model):
    class Meta:
        abstract = True

    uuid = models.CharField(max_length=6, default=uid)

    def save(self, *args, **kwargs):
        old_path = '/%s' % self.uuid
        # using Redirect to enforce uuid uniqueness as using a unique field is prone to validation errors on page revisions
        existing_redirect = Redirect.objects.filter(old_path=old_path).first()
        if existing_redirect and existing_redirect.redirect_page.id == self.id:
            super(UUIDMixin, self).save(*args, **kwargs)
        else:
            self.uuid = uid()
            super(UUIDMixin, self).save(*args, **kwargs)

            old_path = '/%s' % self.uuid
            redirect = Redirect.objects.filter(old_path=old_path).first()
            if not redirect:
                Redirect(old_path=old_path, redirect_page=self).save()
            else:
                self.save(*args, **kwargs)


class ReportChildMixin(models.Model):
    class Meta:
        abstract = True

    @cached_property
    def publication_downloads_title(self):
        return 'Downloads'

    @cached_property
    def publication_downloads_list(self):
        return get_downloads(self, with_parent=True)

    @cached_property
    def data_downloads_title(self):
        return 'Data downloads'

    @cached_property
    def data_downloads_list(self):
        return get_downloads(self, with_parent=True, data=True)

    @cached_property
    def page_publication_downloads(self):
        return self.publication_downloads.all()

    @cached_property
    def page_data_downloads(self):
        return self.data_downloads.all()


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


class ReportDownloadMixin(models.Model):
    class Meta:
        abstract = True

    download_report_cover = WagtailImageField(verbose_name='Report cover')
    download_report_title = models.CharField(
        max_length=255, null=True, blank=True,
        default="Download this report", verbose_name='Section title')
    download_report_body = models.TextField(null=True, blank=True, verbose_name='Section body')
    download_report_button_text = models.CharField(
        max_length=255, null=True, blank=True,
        default="Download now", verbose_name='Button caption')
    report_download = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


class InheritCTAMixin(models.Model):
    """
    Used by child pages of the PublicationPage to inherit Call To Action
    """
    class Meta:
        abstract = True

    @cached_property
    def call_to_action(self):
        return self.get_parent().specific.publication_cta.filter(inherit=True)


class HeroButtonMixin(models.Model):
    download_button_caption = models.CharField(
        max_length=100, default="Downloads", blank=True, null=True, verbose_name='Downloads')
    read_online_button_text = models.CharField(
        max_length=256, default="Read Online", blank=True, null=True, verbose_name='Read Online')
    request_hard_copy_text = models.CharField(
        max_length=256, default="Request a hard copy", blank=True,
        null=True, verbose_name='Read Hard Copy')

    class Meta:
        abstract = True

class RelatedLinksMixin(models.Model):
    related_option_handler = models.CharField(
        max_length=253, choices=RELATED_CHOICES, default='manual', verbose_name='Show By')

    class Meta:
        abstract = True

    def get_related_links(self, objects=None):
        if not objects:
            return None

        if self.related_option_handler == 'topic' or self.related_option_handler == 'Topic':
            combined_queryset = []
            for key in objects:
                results = objects[key].live().filter(topics__in=self.topics.get_queryset()).exclude(id=self.id).distinct()
                for item in results:
                    combined_queryset.append(item)
            slice_queryset = combined_queryset[:MAX_RELATED_LINKS] if len(combined_queryset) > MAX_RELATED_LINKS else combined_queryset
            return get_related_pages(self, slice_queryset, objects)
        elif self.related_option_handler == 'country'  or self.related_option_handler == 'Country':
            countries = [country.country.name for country in self.page_countries.all()]
            combined_queryset = []
            for key in objects:
                results = objects[key].live().filter(page_countries__country__name__in=countries).exclude(id=self.id).distinct()
                for item in results:
                    combined_queryset.append(item)
            slice_queryset = combined_queryset[:MAX_RELATED_LINKS] if len(combined_queryset) > MAX_RELATED_LINKS else combined_queryset
            return get_related_pages(self, slice_queryset, objects)
        elif self.related_option_handler == 'manual' or self.related_option_handler == 'Manual':
            return get_related_pages(self, self.publication_related_links.all(), objects)
