from django.db import models

from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import ChoiceBlock, ListBlock

from di_website.common.constants import INSTRUCTIONS_RICHTEXT_FEATURES, SIMPLE_RICHTEXT_FEATURES
from di_website.publications.utils import WagtailImageField


class GeneralInstructionsMixin(models.Model):
    class Meta:
        abstract = True

    instructions = RichTextField(
        blank=True,
        features=INSTRUCTIONS_RICHTEXT_FEATURES + SIMPLE_RICHTEXT_FEATURES,
    )


class InstructionsMixin(GeneralInstructionsMixin):
    class Meta:
        abstract = True

    instructions_heading = models.TextField(
        blank=True, default='Interactive visualisation instructions',
        verbose_name='Accordion heading')


class SpecificInstructionsMixin(InstructionsMixin):
    class Meta:
        abstract = True

    display_general_instructions = models.BooleanField(
        default=True,
        help_text='Optional: display the general visualisation instructions, edited on the visualisations parent page',
        verbose_name='Show general instructions'
    )


class ChartOptionsMixin(models.Model):
    class Meta:
        abstract = True

    selectable = models.BooleanField(
        default=False,
        help_text='Optional: selectable charts individusalise the data display a dropdown to select data'
    )
    aggregated = models.BooleanField(
        default=False,
        help_text='Optional: aggregated charts adds an "All data" option to selectable charts'
    )
    selector_includes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to include in the dropdown selector. Use when inclusions are fewer than exclusions'
    )
    selector_excludes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to exclude in the dropdown selector. Use when exclusions are fewer than inclusions'
    )
    aggregation_includes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to include in the aggregated chart. Use when inclusions are fewer than exclusions'
    )
    aggregation_excludes = models.TextField(
        null=True, blank=True,
        help_text='Optional: comma separated values to exclude in the aggregated chart. Use when exclusions are fewer than inclusions'
    )
    aggregate_option_label = models.CharField(
        null=True, blank=True, default='All data', max_length=255,
        help_text='The label of the "All data" option on aggregated charts'
    )
    y_axis_prefix = models.CharField(
        null=True, blank=True, max_length=200, help_text='Optional: e.g. UGX, $ e.t.c'
    )
    y_axis_suffix = models.CharField(
        null=True, blank=True, max_length=200, help_text='Optional: e.g. %, degrees e.t.c'
    )
    image_caption = models.TextField(
        null=True, blank=True,
        help_text='Optional: appears in the image download at the bottom of the chart. If blank, the chart title is used instead'
    )
    source = models.TextField(
        null=True, blank=True,
        help_text='Optional: appears in the image download at the bottom of the chart'
    )


class FallbackImageMixin(models.Model):
    class Meta:
        abstract = True

    fallback_image = WagtailImageField(
        required=True,
        help_text='Fallback image for the chart',
    )
    display_fallback_mobile = models.BooleanField(
        default=True,
        help_text='Optional: when selected devices with screen widths up to 400px will be served the fallback image',
        verbose_name='Show on mobile'
    )
    display_fallback_tablet = models.BooleanField(
        default=False,
        help_text='Optional: when selected devices with screen widths up to 700px will be served the fallback image',
        verbose_name='Show on tablet'
    )


class PlotlyOptionsMixin(models.Model):
    class Meta:
        abstract = True

    PLOTLY_BUNDLES = [
        ('basic', 'Basic'),
        ('cartesian', 'Cartesian')
    ]

    use_plotly = models.BooleanField(default=False, blank=True, verbose_name='Use Plotly')
    plotly_bundle = models.CharField(
        max_length=100,
        choices=PLOTLY_BUNDLES,
        blank=True,
        verbose_name='Plotly Bundle',
        default='basic',
        help_text="https://github.com/plotly/plotly.js/blob/master/dist/README.md#partial-bundles"
    )


class D3OptionsMixin(models.Model):
    class Meta:
        abstract = True

    D3_MODULES = [
        ('colour', 'Colour'),
        ('interpolate', 'Interpolate'),
        ('scale-chromatic', 'Scale Chromatic'),
    ]

    D3_VERSIONS = [
        ('v4', 'Version 4'),
        ('v5', 'Version 5'),
        ('v6', 'Version 6'),
    ]

    use_d3 = models.BooleanField(default=False, blank=True, verbose_name='Use D3')
    d3_version = models.CharField(default='v4', max_length=50, choices=D3_VERSIONS, verbose_name='D3 Version')
    d3_modules = StreamField([
        ('module', ChoiceBlock(label='Module', choices=D3_MODULES))
    ], blank=True, verbose_name='D3 Modules')


class EChartOptionsMixin(models.Model):
    class Meta:
        abstract = True

    use_echarts = models.BooleanField(default=False, blank=True, verbose_name='Use ECharts')
