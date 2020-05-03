from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join

from wagtail.core.blocks import StreamBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock


class AudioMediaBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'video':
            player_code = '''
            <h1 class="audio-player-title">Watch to video</h1>
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
                <audio controls='controls' preload='auto' autoplay='autoplay' class='audio-tag'>
                    {0}
                    Your browser does not support audio using the HTML 5 audio element.
                </audio>
                <div>
                    <a download href="{1}" class='download-audio'>Download Audio</a>
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


class AudioMediaStreamBlock(StreamBlock):
    media = AudioMediaBlock()

    required = False
