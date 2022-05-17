# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# Internal:
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestOrderModel(TestCase):
    """
    test the profiles model
    """
    def setUp(self):
        """
        Create a user
        """
        testuser = User.objects.create_user(
            username='ckcabs',
            password='password1',
            email='ckcabs@hotmail.com')
        testuser.save()

    def test_profile_stringmethod_returns_order_num(self):
        """
        test profile model string method
        """
        testuser = User.objects.get(username='ckcabs')
        profile = UserProfile.objects.get(user=testuser)
        self.assertEqual(str(profile), profile.user.username)
