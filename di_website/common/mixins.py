import datetime
from django.core.exceptions import ValidationError
from django.db import models
from wagtail.core.models import Page
from wagtail.contrib.redirects.models import Redirect
from wagtail.search import index
from common.templatetags.string_utils import uid


class UniquePageMixin(object):
    @classmethod
    def can_create_at(cls, parent) -> bool:
        return super(UniquePageMixin, cls).can_create_at(parent) \
            and not cls.objects.exists()


class PageSearchMixin(object):
    search_fields = Page.search_fields + [
        index.SearchField('content', partial_match=True),
    ]


def CustomPageSearchFields(fields):
    return Page.search_fields + [index.SearchField(x, partial_match=True) for x in fields]


class PublishedDateMixin(models.Model):
    class Meta:
        abstract = True

    published_date = models.DateTimeField(
        blank=True,
        help_text='This date will be used for display and ordering',
    )

    def save(self, *args, **kwargs):
        if not self.published_date:
            self.published_date = datetime.datetime.now()
        super().save(*args, **kwargs)


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
            super().save(*args, **kwargs)
        except ValidationError:
            self.uuid = uid()
            super().save(*args, **kwargs)

        old_path = '/%s' % self.uuid
        redirect = Redirect.objects.filter(old_path=old_path).first()
        if not redirect:
            Redirect(old_path=old_path, redirect_page=self).save()
