# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from products.models import Category
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCategoryModel(TestCase):
    """Test Cetegory model"""
    def setUp(self):
        self.category = Category.objects.create(
            name="Courses",
            friendly_name="Courses",
        )

    def test_category_model_str_method(self):
        """ Test Category model string method """
        category = self.category
        self.assertEqual((category.__str__()), category.name)

    def test_category_model_function_friendly_name(self):
        """ Test category model function friendly
            returns friendly name
        """
        category_friendly_name = self.category.friendly_name
        self.assertEqual(str(category_friendly_name), "Courses")
