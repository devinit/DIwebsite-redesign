from django.db import models
from django.utils.text import slugify

from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


@register_snippet
class JobTitle(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'


@register_snippet
class Department(ClusterableModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, help_text="Optional. Will be auto-generated from name if left blank.")

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)


class SubscriptionManager(models.Manager):
    def create_subscription(self, email, subscribe_to, department):
        subscription = self.create(email=email, subscribe_to=subscribe_to, department=department)

        return subscription


class Subscription(models.Model):
    """
    Contacts of individuals who subscribe to updates
    """
    department = ParentalKey(
        Department,
        related_name='department_subscriptions',
        on_delete=models.CASCADE,
        null=True
    )
    email = models.EmailField(max_length=255, blank=False)
    SUBSCRIBE_TO = [
        ('jobs', 'Jobs'),
        ('posts', 'Posts'),
        ('newsletter', 'Newsletter')
    ]
    subscribe_to = models.CharField(
        max_length=100,
        choices=SUBSCRIBE_TO
    )

    def __str__(self):
        return self.email + 'subscribed to' + self.subscribe_to

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    objects = SubscriptionManager()
