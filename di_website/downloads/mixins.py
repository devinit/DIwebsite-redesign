from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class DownloadGroupMixin(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(
        max_length=255,
        help_text='Title of the download group, e.g. "Appendices"',
    )
    singular_name = models.CharField(
        max_length=255,
        help_text='The singular name of the download type. Appended to "Download" to create consistent button labels, e.g. "Download appendix"',
    )

    @property
    def is_valid(self):
        for item in self.downloads:
            if item.value[0].get('file'):
                return True
        return False

    panels = [
        FieldPanel('title'),
        FieldPanel('singular_name'),
        StreamFieldPanel('downloads'),
    ]
