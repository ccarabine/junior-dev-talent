# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    billing information and order history
    """

    user = models.OneToOneField(
        User,
        related_name="user_profile",
        on_delete=models.CASCADE
        )
    is_hiring_manager = models.BooleanField(
        default=False
        )
    default_full_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default=""
        )
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
        )
    default_email = models.EmailField(
        max_length=500,
        blank=True,
        null=True,
        default=""
        )
    location = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=""
        )
    short_intro = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )
    about = models.TextField(
        blank=True,
        null=True,
        default=""
        )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='media/',
        default="default_user.png"
        )
    cv_file = models.FileField(
        null=True,
        blank=True,
        upload_to='media/documents'
        )
    github_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=""
        )
    linkedin_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=""
        )
    created = models.DateTimeField(
        auto_now_add=True,
        )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

class Skill(models.Model):
    """
    A skill model for skill of the user
    """
    owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )
    created = models.DateTimeField(
        auto_now_add=True
        )
   
    def __str__(self):
        return str(self.name)