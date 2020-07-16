from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
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
        FieldPanel('y_axis_suffix', heading='Y-axis suffix')
    ], heading='Chart options')


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
