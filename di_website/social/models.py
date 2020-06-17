from wagtailmetadata.models import MetadataMixin
from django.conf import settings


class MetadataPageMixin(MetadataMixin):

    def get_meta_image(self):
        if getattr(self, 'image', None):
            return self.build_absolute_uri(
                self.image.get_rendition('fill-800x450').url)
        elif settings.CUSTOM_META_DEFAULT_IMAGE:
            return self.build_absolute_uri(settings.CUSTOM_META_DEFAULT_IMAGE)
        return super(MetadataPageMixin, self).get_meta_image()

    def get_meta_description(self):
        return self.search_description if self.search_description else self.title

    def get_meta_title(self):
        return None

# TODO: add new override functions to get decent social descriptions for FB, Twitter etc using page search_description or title
