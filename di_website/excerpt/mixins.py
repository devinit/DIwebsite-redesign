import bleach
from django.db import models
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe
from django.utils.text import Truncator


class BaseExcerptMixin(models.Model):
    class Meta:
        abstract = True

    @cached_property
    def excerpt(self) -> str:
        try:
            if self.excerpt_field != '':
                return self.excerpt_field
            else:
                return self.get_stripped_content
        except AttributeError:
            try:
                return self.get_stripped_content
            except AttributeError:
                return ''

    @cached_property
    def get_stripped_content(self):
        return (Truncator(strip_tags(self.content))
                .words(30)
                .replace('.', '. ')
                .replace('?', '? ')
                .replace('. . . ', '...'))


class ExcerptMixin(BaseExcerptMixin):
    class Meta:
        abstract = True

    excerpt_field = models.TextField(
        blank=True,
        verbose_name='Excerpt',
    )


def strip_tags(text) -> str:
    return mark_safe(bleach.clean(
        text,
        tags=[],
        attributes=[],
        styles=[],
        strip=True,
        strip_comments=True
    ))


class ExcerptMixinNoField(models.Model):
    class Meta:
        abstract = True
