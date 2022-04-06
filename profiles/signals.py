# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import UserProfile


def create_user(sender, instance, created, **kwargs):
    """
        Sends an email to the user when a user signs up
        Args:
            sender: sender
            instance: instance (user)
            created: created date
            **kwargs: **kwargs
        Returns:
            N/A
        """
    if created:
        user = instance
        UserProfile.objects.create(
            user=instance)

        subject = 'Welcome to Junior Dev Talent'
        message = 'Thank you for joining Junior Dev Talent'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    # Existing users: just save the profile
    instance.user_profile.save()


def delete_user(sender, instance, **kwargs):
    """
    Delete a user when a profile is deleted
    Args:
        sender: sender
        instance: instance (user)
        **kwargs: **kwargs
    Returns:
        N/A
    """
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(create_user, sender=User)
post_delete.connect(delete_user, sender=UserProfile)
