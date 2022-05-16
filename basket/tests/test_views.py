# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
# Internal:
from products.models import Product, Category
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBasketView(TestCase):
    """Test Basket View"""
    def setUp(self):
        self.client = Client()
        User.objects.create(username='chris')
        Category.objects.create(name='course')
        
        self.product = Product.objects.create(
            name='c++',
            price='45.00',
            description='course description',
            category=Category.objects.all()[0])
        
    def test_get_bag_page(self):
        """
        This test checks that the basket page is displayed
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
    
    def test_add_to_bag(self):
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