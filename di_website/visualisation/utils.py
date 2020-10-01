from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from di_website.common.edit_handlers import HelpPanel

def ChartOptionsPanel():
    return MultiFieldPanel([
        FieldPanel('selectable'),
        FieldPanel('selector_includes'),
        FieldPanel('selector_excludes'),
        FieldPanel('aggregated'),
        FieldPanel('aggregation_includes', classname='full'),
        FieldPanel('aggregation_excludes', classname='full'),
        FieldPanel('aggregate_option_label', classname='full full-custom'),
        FieldPanel('y_axis_prefix', heading='Y-axis prefix'),
        FieldPanel('y_axis_suffix', heading='Y-axis suffix'),
        FieldPanel('image_caption'),
        FieldPanel('source')
    ], heading='Chart options')


def InstructionsPanel():
    return MultiFieldPanel(
        [
            FieldPanel('instructions_heading'),
            FieldPanel('instructions'),
        ],
        heading='Interactive visualisation instructions',
    )


def SpecificInstructionsPanel():
    return MultiFieldPanel(
        [
            HelpPanel('''
                Optional: if the checkbox is selected, the general instructions from the parent page will be displayed.<br>
                Specific instuctions added to this page will be displayed, overriding this setting.
            ''', wrapper_class='help-block help-info no-padding-top'),
            FieldPanel('display_general_instructions'),
            FieldPanel('instructions_heading'),
            FieldPanel('instructions'),
        ],
        heading='Interactive visualisation instructions',
    )

def FallbackImagePanel():
    return MultiFieldPanel([
            ImageChooserPanel('fallback_image'),
            FieldPanel('display_fallback_mobile'),
            FieldPanel('display_fallback_tablet'),
        ], heading='Fallback image and options')


def PlotlyOptionsPanel():
    return MultiFieldPanel(
        [
            HelpPanel('''
                Optional: if plotly is selected, please be sure to specify which bundle to load depending the type of chart you are building<br>
                This will ensure only the relevant optimised code gets loaded.
            ''', wrapper_class='help-block help-info no-padding-top'),
            FieldPanel('use_plotly'),
            FieldPanel('plotly_bundle')
        ],
        classname='collapsible',
        heading='Plotly Options',
    )


def D3OptionsPanel():
    return MultiFieldPanel(
        [
            FieldPanel('use_d3'),
            FieldPanel('d3_version'),
            StreamFieldPanel('d3_modules'),
        ],
        classname='collapsible',
        heading='d3 Options',
    )


def EChartOptionsPanel():
    return MultiFieldPanel(
        [
            FieldPanel('use_echarts')
        ],
        classname='collapsible',
        heading='EChart Options',
    )
