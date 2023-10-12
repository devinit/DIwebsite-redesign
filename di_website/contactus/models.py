from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page

from di_website.common.base import hero_panels
from di_website.common.mixins import HeroMixin, TypesetBodyMixin


class ContactPage(TypesetBodyMixin, HeroMixin, Page):
    """
        Contact us page.
    """
    template = 'contactus/contact_page.html'
    landing_template = 'contactus/contact_page_landing.html'

    content_panels = Page.content_panels + [
        hero_panels(),
        FieldPanel('body'),
        InlinePanel('page_notifications', label='Notifications')
    ]

    class Meta():
        verbose_name = 'Contact Us Page'

    subpage_types = ['general.General']
    parent_page_types = ['home.HomePage']
