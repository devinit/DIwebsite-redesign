from wagtail.admin.panels import HelpPanel as WagtailHelpPanel


def HelpPanel(
    content='',
    template='wagtailadmin/panels/help_panel.html',
    heading='',
    classname='',
    wrapper_class='help-block help-info'
):
    """Define a help text panel."""
    wrapped_content = '<div class="%s"><svg class="icon icon-help" aria-hidden="true"><use href="#icon-help"></use></svg>%s</div>' % (wrapper_class, content)
    return WagtailHelpPanel(content=wrapped_content, template=template, heading=heading, classname=classname)
