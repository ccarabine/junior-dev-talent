# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import UserProfile


class UserAccountForm(forms.ModelForm):
    """
    A class for the user profile form
    """
    class Meta:
        """
        A class for the Meta information
        """
        model = UserProfile
        exclude = ('user', 'is_hiring_manager',
                   'location',
                   'short_intro', 'about',
                   'profile_image', 'cv_file',
                   'github_link', 'linkedin_link',
                   )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County'

        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-blue rounded-0 profile-form-input'
            self.fields[field].label = False


class UserProfileForm(forms.ModelForm):
    """
    A class for the user account form
    """
    class Meta:
        """
        A class for the Meta information
        """
        model = UserProfile
        exclude = ('user',  'is_hiring_manager',
                   'default_full_name',
                   'default_email',
                   'default_phone_number',
                   'default_postcode',
                   'default_town_or_city',
                   'default_street_address1',
                   'default_street_address2',
                   'default_country',
                   'default_county')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {

            'location': 'location',
            'short_intro': 'Job title',
            'about': 'About',
            'profile_image': 'Profile Image',
            'cv_file': 'CV',
            'github_link': 'Github URL',
            'linkedin_link': 'Linkedin URL',
        }

        self.fields['location'].widget.attrs['autofocus'] = True
        for field in self.fields:

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-blue rounded-0 profile-form-input'
            self.fields[field].label = False
