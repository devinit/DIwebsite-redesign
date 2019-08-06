from django.forms.utils import pretty_name
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import EditHandler
from django.utils.html import mark_safe

class BaseReadOnlyPanel(EditHandler):

    def render(self):
        value = getattr(self.instance, self.field_name)
        if callable(value):
            value = value()
        return format_html('<div style="padding-top: 1.2em;">{}</div>', mark_safe(value))

    def render_as_object(self):
        return format_html(
            '<fieldset><legend>{}</legend>'
            '<ul class="fields"><li><div class="field">{}</div></li></ul>'
            '</fieldset>',
            self.heading, self.render())

    def render_as_field(self):
        return format_html(
            '<div class="field">'
            '<label>{}{}</label>'
            '<div class="field-content">{}</div>'
            '</div>',
            self.heading, _(':'), self.render())


"""
Custom implementation of readonly panel, refer to issue on from wagtail
https://github.com/wagtail/wagtail/issues/2893

"""
class ReadOnlyPanel(BaseReadOnlyPanel):

    def __init__(self,field_name,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.field_name = field_name

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            field_name=self.field_name
        )
        return kwargs

    def bind_to_model(self, model):
        return type(str(_('ReadOnlyPanel')), (BaseReadOnlyPanel,),
                    {'model': self.model, 'heading': self.heading, 'classname': self.classname})
