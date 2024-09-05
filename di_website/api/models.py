from django.db import models
from wagtail.snippets.models import register_snippet

# Create your models here.

@register_snippet
class CookieConsentLogEntry(models.Model):
    token = models.CharField(max_length=255, primary_key=True)
    anonymised_ip_address = models.GenericIPAddressField()
    first_seen = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    url = models.URLField()
    user_agent = models.TextField()
    choice = models.CharField(max_length=255)


    def __str__(self):
        return self.token or 'Unknown log entry'

    class Meta():
        verbose_name = "Cookie Consent Log Entry"
        verbose_name_plural = "Cookie Consent Log Entries"
