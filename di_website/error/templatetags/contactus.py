from django import template

from di_website.contactus.models import ContactPage

from .context import globals


register = template.Library()


@register.inclusion_tag('tags/contact_us_link.html', takes_context=True)
def load_contactus(context):
    global_obj = globals(context['request'])
    contactus = ContactPage.objects.live().first()
    return {'contactus_page': contactus, 'global': global_obj['global']}
