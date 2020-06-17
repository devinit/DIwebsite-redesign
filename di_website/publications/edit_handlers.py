import glob
import os
import re
from django.conf import settings
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import MultiFieldPanel as WagtailMultiFieldPanel
import logging

logger = logging.getLogger('file')


class ThemeFieldPanel(FieldPanel):

    def get_theme_options(self):
        options = [('', 'None',)]

        for filename in glob.glob(os.path.join(settings.THEMES, '*.css')):
            try:
                with open(filename, 'r') as f:
                    name = os.path.basename(f.name)
                    lines = f.readlines()
                    first_line = lines[0]
                    f.close()
                    if r'/*' in first_line and r'*/' in first_line:
                        title = re.sub(r'[^A-Za-z0-9 ]+', '', first_line).strip()
                        if title:
                            options.append((name, title,))
                    else:
                        continue

            except (FileNotFoundError, IndexError):
                print('error')
                logger.exception('Error in ThemeFieldPanel')
                pass

        return options

    def on_form_bound(self):

        try:
            choices = self.get_theme_options()
            self.form.fields[self.field_name].widget.choices = choices
        except Exception:
            pass

        super().on_form_bound()


class MultiFieldPanel(WagtailMultiFieldPanel):
    def __init__(self, children=(), *args, **kwargs):
        if kwargs.get('description', None):
            self.description = kwargs.pop('description')
        super().__init__(children, *args, **kwargs)

    def clone(self):
        props = {
            'children': self.children,
            'heading': self.heading,
            'classname': self.classname,
            'help_text': self.help_text,
        }
        if hasattr(self, 'description'):
            props['description'] = self.description
        return self.__class__(**props)
