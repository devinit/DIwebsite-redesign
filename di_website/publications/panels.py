from django import forms
from wagtail.admin.edit_handlers import FieldPanel
from .edit_handlers import MultiFieldPanel
from .edit_handlers import ThemeFieldPanel


def ThemePanel(
    heading='Theme',
    description='Optional: select a custom theme to override the style of this report and associated child pages.'
):
    return MultiFieldPanel(
        [
            ThemeFieldPanel('report_theme', classname='non-floated-options', widget=forms.RadioSelect),
        ],
        heading=heading,
        description=description
    )


def HighlightPanel(
    heading='Highlight',
    description='Optional: highlight this page\'s image on the main report page using theme-specific style (highlight only applies to custom themed report pages).'
):
    return MultiFieldPanel(
        [
            FieldPanel('highlight_image'),
        ],
        heading=heading,
        description=description
    )
