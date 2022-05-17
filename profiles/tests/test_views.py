# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.contrib.auth.models import User

# Internal:
from checkout.models import Order
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestTopicModel(TestCase):
    """
    Test the profile page loads correctly
    """
    def setUp(self):
        self.client = Client()
        testuser = User.objects.create_user(
            username="ckcabs", email="ckcabs@hotmail.com",
            password="123abcde4"
            )
        Order.objects.create(
            order_number='65595858',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Chris Carabine',
            email='ckcabs@hotmail.com',
            phone_number='07773323840',
            country='GB',
            postcode='TW2 5RZ',
            town_or_city='Twickenham',
            street_address1='Flat 1 67 Wellesley Rd',
            county='London',
        )

    def test_profile_page_url_works(self):
        """
        Test the url works when loading the page
        """
        self.client.login(username="ckcabs",
                          email="ckcabs@hotmail.com", password="123abcde4")
        response = self.client.get('/profiles/display_profile')
        self.assertEqual(response.status_code, 200)

    def test_order_detail_page(self):
        """
        This test logins a  user and accesses
        the order history page for a test order and verifies
        """
        self.client.login(username='ckcabs', password='123abcde4')
        order = Order.objects.get(email='ckcabs@hotmail.com')
        response = self.client.get('/profiles/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
