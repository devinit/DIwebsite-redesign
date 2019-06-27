from django.db import models
from django.contrib.auth.models import AbstractUser
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel


DEPARTMENTS = [
    ("LEA", "Leadership Team"),
    ("DAT", "Data Science & Information Architecture"),
    ("REA", "Research & Analysis"),
    ("PRO", "Project Management"),
    ("HRF", "HR, Facilities, IT & Finance"),
    ("STR", "Strategic Partnerships"),
    ("COM", "Communications"),
    ("POL", "Policy & Engagement"),
    ("NON", "Non-Executive Directors"),
    ("BOA", "Board Members"),
    ("CON", "Consultants"),
    ("FEL", "Fellow")
]


@register_snippet
class UserProfile(models.Model):
    user = models.OneToOneField(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    position = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=3, choices=DEPARTMENTS, null=True, blank=True)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    active = models.BooleanField(default=False, help_text="Should this user's profile be displayed as staff?")

    panels = [
        FieldPanel('user'),
        ImageChooserPanel('image'),
        FieldPanel('position'),
        FieldPanel('department'),
        PageChooserPanel('page'),
        FieldPanel('active')
    ]

    def __str__(self):
        return "{} ({})".format(self.name if self.name else self.user.username, "Active" if self.active else "Inactive")


class User(AbstractUser):
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        profile, _ = UserProfile.objects.get_or_create(user=self)
        profile.name = self.get_full_name()
        profile.save()
