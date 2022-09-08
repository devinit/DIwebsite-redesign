from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join
from wagtail.core.blocks import (ListBlock, RichTextBlock, StreamBlock,
                                 StructBlock, TextBlock)
from wagtailmedia.blocks import AbstractMediaChooserBlock

from di_website.common.constants import RICHTEXT_FEATURES


class AudioMediaBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'video':
            player_code = '''
            <h1 class="audio-player-title">Watch video</h1>
            <div>
                <video width="320" height="240" controls>
                    {0}
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
        else:
            player_code = '''
            <h1 class="audio-player-title">Listen to audio</h1>
            <div>
                <audio controls='controls' preload='auto' class='audio-tag'>
                    {0}
                    Your browser does not support audio using the HTML 5 audio element.
                </audio>
                <div>
                    <a download href="{1}" class='download-audio'>Download audio</a>
                </div>
            </div>
            '''

        return format_html(player_code, format_html_join(
            '\n', "<source{0}>",
            [[flatatt(s)] for s in value.sources]
        ),
        value.sources[0].get('src'))

    class Meta():
        icon = 'media'
        label = 'Audio'


class AudioMediaStreamBlock(StreamBlock):
    media = AudioMediaBlock()

    required = False

class GlossaryAccordionBlock(StructBlock):
    items = ListBlock(StructBlock([
        ('title', TextBlock(icon='fa-text')),
        ('description', RichTextBlock(
            icon='fa-paragraph',
            template='blocks/paragraph_block.html',
            features=RICHTEXT_FEATURES,
            required=False))
    ]))
