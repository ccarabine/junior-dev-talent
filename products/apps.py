# pylint: disable=missing-module-docstring
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig

# Internal:


class ProductsConfig(AppConfig):
    """
    A class for the products configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
