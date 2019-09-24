from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property


from wagtail.core.models import Page
from wagtail.contrib.redirects.models import Redirect
from wagtail.search import index

from di_website.common.templatetags.string_utils import uid

from .fields import flexible_content_streamfield, content_streamfield
from .utils import get_downloads


class UniquePageMixin(object):
    @classmethod
    def can_create_at(cls, parent) -> bool:
        return super(UniquePageMixin, cls).can_create_at(parent) and not cls.objects.exists()


class ParentPageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.SearchField('title', partial_match=True),
        index.FilterField('slug')
    ]


class PageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.SearchField('content', partial_match=True),
        index.SearchField('title', partial_match=True),
        index.FilterField('slug')
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

    uuid = models.CharField(
        max_length=6,
        unique=True,
        default=uid,
    )

    def save(self, *args, **kwargs):
        try:
            super(UUIDMixin, self).save(*args, **kwargs)
        except ValidationError:
            self.uuid = uid()
            super(UUIDMixin, self).save(*args, **kwargs)

        old_path = '/%s' % self.uuid
        redirect = Redirect.objects.filter(old_path=old_path).first()
        if not redirect:
            Redirect(old_path=old_path, redirect_page=self).save()


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
