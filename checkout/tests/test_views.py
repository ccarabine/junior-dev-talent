# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.messages import get_messages
# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutViews(TestCase):
    """
    Tests the view in the checkout app
    """

    def test_checkout_page_url_works(self):
        """
        This Test the url works when loading the page
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """
        This test the correct template loads on page load
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_checkout_view_empty_basket(self):
        """
        This test test an empty basket for checkout and verifies
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your basketat the moment")
