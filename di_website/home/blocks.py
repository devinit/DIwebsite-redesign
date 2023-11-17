from wagtail.blocks import (CharBlock, PageChooserBlock, RichTextBlock,
                            StreamBlock, StructBlock)
from di_website.common.constants import RICHTEXT_FEATURES_NO_FOOTNOTES


class FeaturedContentBlock(StreamBlock):
    content = StructBlock([
            ('title', CharBlock()),
            ('body', RichTextBlock(features=RICHTEXT_FEATURES_NO_FOOTNOTES)),
            ('related_page', PageChooserBlock(required=False)),
            ('button_caption', CharBlock(required=False, help_text='Overwrite title text from the related page'))
        ], template='home/blocks/featured_content.html',)

    class Meta:
        template = 'home/blocks/featured_content.html'


class FeaturedWorkBlock(StructBlock):
    featured_work_heading = CharBlock(
        blank=True,
        null=True,
        default='Featured work',
        max_length=200,
        verbose_name='Section heading'
    )
    featured_pages = StreamBlock([('featured_page', PageChooserBlock())])

    class Meta:
        template = 'home/blocks/featured_work.html'
