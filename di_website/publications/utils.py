from collections import defaultdict

from django.db import models

from di_website.common.constants import MAX_RELATED_LINKS

from wagtail.admin.panels import FieldPanel, InlinePanel

from .edit_handlers import MultiFieldPanel


def get_downloads(instance, with_parent=False, data=False):
    d = defaultdict(list)
    downloads = instance.data_downloads.all() if data else instance.publication_downloads.all()

    for item in downloads:
        download = create_download(item)
        if download[1]['download'] is not None:
            d[download[0]].append(download[1])

    if with_parent:
        if data:
            parent_downloads = instance.get_parent().specific.data_downloads.all()
        else:
            parent_downloads = instance.get_parent().specific.publication_downloads.all()

        for item in parent_downloads:
            download = create_download(item)
            d[download[0]].append(download[1])

    return d.items()


def create_download(item):
    download = {
        'prefix': '',
        'download': item.download
    }

    try:
        language = item.download.language.title
    except AttributeError:
        language = ''

    return (language, download, )


def ContentPanel(heading='Content', description='Main content for the page. Build page content by adding new rows from the available content types.'):
    return MultiFieldPanel(
        [
            FieldPanel('content'),
        ],
        heading=heading,
        description=description,
    )


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

def RelatedLinksPanel():
    return MultiFieldPanel([
        FieldPanel('related_option_handler', heading='Show by'),
        InlinePanel('publication_related_links', label='Related links', max_num=MAX_RELATED_LINKS)
    ], heading='Related Links', help_text="Displays only publications, podcasts, blogs and news stories")

def StateMixinPanel():
    return FieldPanel('use_state')


def ReportDownloadPanel():
    return MultiFieldPanel([
        FieldPanel('download_report_title'),
        FieldPanel('download_report_body'),
        FieldPanel('download_report_cover'),
        FieldPanel('report_download')
    ], heading='Report download section')


def HeroButtonPanel(heading='Hero Button Captions', description='Edit captions for hero buttons'):
    return MultiFieldPanel(
        [
            FieldPanel('download_button_caption'),
            FieldPanel('read_online_button_text'),
            FieldPanel('request_hard_copy_text'),
        ],
        heading=heading,
        description=description
    )


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
