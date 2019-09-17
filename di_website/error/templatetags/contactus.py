from django import template

from di_website.contactus.models import ContactPage

register = template.Library()


@register.inclusion_tag('tags/contact_us_link.html')
def load_contactus():
    contactus = ContactPage.objects.live().first()
    return {'contactus_page': contactus}
