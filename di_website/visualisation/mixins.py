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
