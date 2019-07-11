from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from di_website.ourteam.models import TeamMemberPage


@register_snippet
class JobTitle(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'


@register_snippet
class Department(models.Model):
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


@register_snippet
class UserProfile(models.Model):
    # TODO: add paragraph when added to common
    user = models.OneToOneField(
        User,
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
    position = models.ForeignKey(
        JobTitle,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    telephone = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=False, help_text="Should this user's profile be displayed as staff?")

    panels = [
        FieldPanel('user'),
        FieldPanel('name'),
        ImageChooserPanel('image'),
        SnippetChooserPanel('position'),
        SnippetChooserPanel('department'),
        PageChooserPanel('page'),
        FieldPanel('email'),
        FieldPanel('telephone'),
        FieldPanel('active')
    ]

    def __str__(self):
        return "{} ({})".format(self.name if self.name else self.user.username, "Active" if self.active else "Inactive")

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new user profile on a post-save."""
    profile, _ = UserProfile.objects.get_or_create(user=instance)
    profile.name = instance.get_full_name()
    if not profile.email:
        profile.email = instance.email
    profile.save()
