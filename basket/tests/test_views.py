# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.messages import get_messages
# Internal:
from products.models import Product, Category
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBasketView(TestCase):
    """Test Basket View"""
    def setUp(self):
        User.objects.create(username='chris')
        Category.objects.create(name='course')

        self.product = Product.objects.create(
            name='c++',
            price='45.00',
            description='course description',
            category=Category.objects.all()[0])

    def test_view_basket_template(self):
        """
        This test checks that the basket template is displayed
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_add_to_basket(self):
        """
        This test checks add product to basket and
        redirects to the products template with a status code of 302
        """
        product = Product.objects.create(
            name='c++',
            price='45.00',
            description='course description',
            image="image_name",
            )
        response = self.client.post(f'/basket/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})

        self.assertRedirects(response, f'/products/{product.id}/')
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Added c++ to your basket")

    def test_adjust_basket(self):
        """
        This test checks that the product course updates to quanity 2
        and a message displayed
        """
        product = Product.objects.get(name='c++')
        response = self.client.post(f'/basket/adjust/{product.id}/',
                                    {'quantity': 2})
        basket = self.client.session['basket']
        self.assertEqual(basket[str(product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Updated c++ quantity to 2')

    def test_adjust_basket_quantity_to_zero(self):
        """
        Tests updating the basket item quantity from 2 to 0
        """
        product = Product.objects.create(
                    name='c++',
                    price='45.00',
                    description='course description',
                    image="image_name",
                    )

        response = self.client.post(f'/basket/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})
        self.assertRedirects(response, '/products/2/')
        basket = self.client.session['basket']
        self.assertEqual(basket[str(product.id)], 1)
        response = self.client.post(f'/basket/adjust/{product.id}/', {
            'quantity': 0, 'redirect_url': 'view_basket'})
        basket = self.client.session['basket']
        self.assertEqual(basket, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Removed c++ from your basket')
