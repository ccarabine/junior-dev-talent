# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin class for the User Profile model.
    """
    fields = (
        'is_hiring_manager',
        'default_full_name',
        'default_phone_number',
        'default_email',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
        'location',
        'short_intro',
        'about',
        'profile_image',
        'cv_file',
        'github_link',
        'linkedin_link',
        )
    
    list_display = ('user','is_hiring_manager','default_full_name')

    ordering = ('default_full_name',)
