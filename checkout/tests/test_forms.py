# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from checkout.forms import OrderForm


class TestPostForm(TestCase):

    def test_full_name_is_required(self):
        """
        This test tests the field "full name" is  required
        checks
        1.form is not valid as full name is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': '',
            'email': 'projectckcabs@gmail.com',
            'phone_number': '07754212111',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': 'Twickenham',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        This test tests the field "email" is  required
        checks
        1.form is not valid as email is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': '',
            'phone_number': '07754212111',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': 'Twickenham',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """
        This test tests the field "phone number" is  required
        checks
        1.form is not valid as full name is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': 'ckcabs@hotmail.com',
            'phone_number': '',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': 'Twickenham',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_street_address_1_is_required(self):
        """
        This test tests the field "street address 1" is  required
        checks
        1.form is not valid as street address 1 is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': 'ckcabs@hotmail.com',
            'phone_number': '07754212111',
            'street_address1': '',
            'town_or_city': 'Twickenham',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    def test_town_or_city_is_required(self):
        """
        This test tests the field "town or city" is  required
        checks
        1.form is not valid as town or city is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': 'ckcabs@hotmail.com',
            'phone_number': '07754212111',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': '',
            'country': 'GB',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_country_is_required(self):
        """
        This test tests the field "country" is  required
        checks
        1.form is not valid as country is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': 'ckcabs@hotmail.com',
            'phone_number': '07754212111',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': 'Twickenham',
            'country': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0],
                         'This field is required.')

    def test_correct_country_code_is_required(self):
        """
        This test tests the field correct country code is  required
        checks
        1.form is not valid as country code is in correct
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': 'ckcabs@hotmail.com',
            'phone_number': '07754212111',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': 'Twickenham',
            'country': 'UK',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0],
            'Select a valid choice. UK is not one of the available choices.')

    def test_form_valid(self):
        """
        This test tests that is form is valid when all
        required fields are completed
        checks
         """
        form = OrderForm({
            'full_name': 'Chris Carabine',
            'email': 'ckcabs@hotmail.com',
            'phone_number': '07773323840',
            'street_address1': 'Flat 2 67 wellesley road',
            'town_or_city': 'Twickenham',
            'postcode': 'TW2 5RZ',
            'country': 'GB',
            'county': 'Greater London',
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_bag_form_metaclass(self):
        """
        This test tests the field in the meta only display
        checks
        1. The field is in meta
        """
        form = OrderForm()
        self.assertEqual(
            form.Meta.fields, ('full_name', 'email',
                               'phone_number', 'street_address1',
                               'street_address2', 'town_or_city', 'postcode',
                               'country', 'county'))
