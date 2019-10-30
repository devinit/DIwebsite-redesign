from bs4 import BeautifulSoup
from django import template
from django.utils.safestring import mark_safe
from common.templatetags.string_utils import content

register = template.Library()


@register.tag(name='content_with_footnotes')
def do_content_with_footnotes(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, rich_text = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires a single argument' % token.contents.split()[0]
        )
    return FootnotesContentNode(rich_text)


class FootnotesContentNode(template.Node):
    def __init__(self, rich_text):
        self.rich_text = template.Variable(rich_text)

    def render(self, context):

        rich_text = content(self.rich_text.resolve(context))

        # get or create a list of footnotes in the context
        footnotes_list = getattr(context.get('page'), 'footnotes_list', [])

        # find and replace footnote spans
        soup = BeautifulSoup(
            rich_text,
            features='html5lib'
        )

        for span in soup.select('span[data-type="footnote"]'):

            # get the tag
            tag = span

            # get the text of the footnote
            text = tag.getText()

            # get the id and refs
            uuid = tag['data-id']
            footnote_id = 'note-%s' % uuid
            footnote_href = '#%s' % footnote_id
            source_id = 'note-source-%s' % uuid

            # add to the footnotes list
            footnotes_list.append({
                'text': text,
                'footnote_id': footnote_id,
                'source_id': source_id,
            })

            # get the position
            position_id = len(footnotes_list)

            # replace the span
            a_tag = soup.new_tag('a', attrs={'href': footnote_href, 'id': source_id, 'aria-describedby': footnote_id})
            sup_tag = soup.new_tag('sup')
            sup_tag.string = '[%s]' % str(position_id)
            a_tag.append(sup_tag)
            tag.replace_with(a_tag)

        # get rid of the soup wrappers
        soup.html.unwrap()
        soup.head.extract()
        soup.body.unwrap()

        try:
            setattr(context['page'], 'footnotes_list', footnotes_list)
        except Exception:
            pass

        return mark_safe(str(soup))
