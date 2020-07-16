from django.db import models
from wagtail.core.fields import RichTextField
from di_website.common.constants import INSTRUCTIONS_RICHTEXT_FEATURES


class GeneralInstructionsMixin(models.Model):
    class Meta:
        abstract = True

    instructions = RichTextField(
        blank=True,
        features=INSTRUCTIONS_RICHTEXT_FEATURES,
    )


class SpecificInstructionsMixin(GeneralInstructionsMixin):
    class Meta:
        abstract = True

    display_general_instructions = models.BooleanField(
        default=True,
        help_text='Optional: display the general visualisation instructions, edited on the visualisations parent page',
        verbose_name='Show instructions'
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
