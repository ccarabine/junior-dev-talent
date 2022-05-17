# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestHomeViews(TestCase):
    """
    Test the home view page
    """
    def test_page_access(self):
        """
        Test the home view page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404_error_page(self):
        """
        Test the 404 error page, when incorrect url is entered
        """
        response = self.client.get('/df')
        self.assertEqual(response.status_code, 404)
