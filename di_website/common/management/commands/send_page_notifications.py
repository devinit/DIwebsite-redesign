import re

from django.utils.html import strip_tags
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

from di_website.common.base import PageNotification

class Command(BaseCommand):
    """
    Finds all active page notifications and sends them via email. Send notifications and then deleted.
    """

    def handle(self, *args, **options):
        current_datetime = timezone.now()
        notifications = PageNotification.objects.filter(date_time__lte=current_datetime)

        for notification in notifications:
            page = notification.page.specific
            message = notification.message.replace('%page_title%', page.title).replace('%page_url%', page.full_url)
            email_list = notification.emails.split(',')
            send_mail(
                notification.title,
                None,
                'no-reply@devinit.org',
                email_list,
                html_message=message,
                fail_silently=False,
            )
            notification.delete()
