from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.modeladmin.helpers import ButtonHelper


def ForeignKeyField(model=None, required=False, on_delete=models.SET_NULL, related_name='+', **kwargs) -> models.ForeignKey:
    if not model:
        raise ValueError('ForeignKeyField requires a valid model string reference')
    required = not required
    return models.ForeignKey(
        model,
        null=True,
        blank=required,
        on_delete=on_delete,
        related_name=related_name,
        **kwargs
    )


def WagtailImageField(required=False, **kwargs) -> models.ForeignKey:
    return ForeignKeyField(
        model='wagtailimages.Image',
        required=required,
        **kwargs
    )


def get_selected_or_fallback(selected=None, fallback=None, max_length=None, order=None) -> list:
    if not selected:
        selected = []
    else:
        # return actual page object instead of through model
        selected = [x.related for x in selected]

    fallbacks = []
    if fallback:
        try:
            fallbacks = fallback
            if selected:
                fallbacks = fallbacks.exclude(
                    id__in=[x.id for x in list(selected)]
                ).live().specific()
            if order:
                fallbacks = fallbacks.order_by(order)
        except AssertionError as e:
            if 'Cannot filter a query once a slice has been taken' in str(e):
                raise Exception('Cannot filter a query once a slice has been taken. \
                             Use the max_length argument if you want to limit the amount returned')

    if not max_length:
        return list(selected) + list(fallbacks)
    else:
        return list(list(selected) + list(fallbacks))[:max_length]


def get_children_or_none(page_query):
    if not page_query:
        return None

    return page_query.get_children().live()


def get_first_child_of_type(parent, child_class):
    return (
        parent.get_children()
        .type(child_class)
        .live()
        .specific()
        .first())


def get_ordered_children_of_type(parent, child_class, order):
    return (
        parent.get_children()
        .type(child_class)
        .live()
        .order_by(order)
        .specific())


def get_specific_related(queryset):
    '''Return related pages from through table queryset.'''
    if not queryset:
        return None

    return [x.related.specific for x in queryset if x.related and x.related.live]


def PublishedDatePanel():
    return MultiFieldPanel(
        [
            FieldPanel('published_date'),
        ],
        heading='Published date',
        description='Date information for this page.',
    )


def UUIDPanel():
    return FieldPanel('uuid')


class UniqueButtonHelper(ButtonHelper):
    def add_button(self, classnames_add=None, classnames_exclude=None):
        if len(self.model.objects.all()):
            return ''
        return super().add_button(classnames_add, classnames_exclude)
