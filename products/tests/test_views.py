# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
# Internal:
from products.models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    This test the product Views
    """
    def setUp(self):
        """
        This create a user, category, product
        """
        User.objects.create_user(
            username='ckcabs', password='password1')

        User.objects.create_superuser(
            username='admin', password='password2')

        Category.objects.create(
            name='courses', friendly_name='course')

        Product.objects.create(
            name='c++',
            price='45.00',
            description='c++ courseTest',
        )

    def test_user_count(self):
        """
        This checks there are two users setup
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_url_response(self):
        """
        This tests that the url response  is success 200
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_get_products_by_search_term(self):
        """
        This tests the search term works and gets a 200 sucess code
        """
        response = self.client.get('/products/', {
            'search_term': 'c++', 'current_categories': 'courses'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_detailed_product_view(self):
        """
        This tests the product details page
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/',
                                   {'product': product})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_superuser_can_add_product(self):
        """
        This tests admin can access the add a product page
        """
        self.client.login(username='admin', password='password2')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_non_superuser_can_not_add_product(self):
        """
        Test non superuser can't access the add a product page
        """
        self.client.login(username='ckcabs', password='password1')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Sorry, only store owners can do that.")
        self.assertEqual(response.status_code, 302)
