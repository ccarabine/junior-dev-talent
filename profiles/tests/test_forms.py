# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from profiles.forms import UserProfileForm, SkillForm


class TestProfileForm(TestCase):

    def test_no_fields_are_required(self):
        """
        This test tests the field no fields are  required

        """
        form = UserProfileForm({
            'is_hiring_manager': '',
            'default_full_name': '',
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_county': '',
            'default_postcode': '',
            'default_country': '',
            'default_email': '',
            'short_intro': '',
            'about': '',
            'location': '',
            'profile_image': '',
            'github_link': '',
            'linkedin_link': '',
            'cv_file': '',
            })
        self.assertTrue(form.is_valid())


class TestSkillForm(TestCase):

    def test_no_fields_are_required(self):
        """
        This test tests the name field is required

        """
        form = SkillForm({
            'name': '',
            })
        self.assertFalse(form.is_valid())
