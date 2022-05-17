# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from checkout.models import Order
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestOrderModel(TestCase):
    """
    test the order model
    """
    def setUp(self):
        """
        Create a test product and order
        """
        Product.objects.create(
            name='c++',
            price='45.00',
            description='cc++ course',
        )

        Order.objects.create(
            full_name='Chris Carabine',
            email='chris@gmail.com',
            phone_number='07773323840',
            country='GB',
            town_or_city='Twickenham',
            street_address1='Flat 1 67 Wellesley road',
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Product.objects.all().delete()
        Order.objects.all().delete()

    def test_order_stringmethod_returns_order_num(self):
        """
        test order model string method
        """
        order = Order.objects.get(email='chris@gmail.com')
        self.assertEqual(str(order), order.order_number)
