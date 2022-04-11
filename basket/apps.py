# pylint: disable=missing-module-docstring
# # Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BasketConfig(AppConfig):
    """
    A class for configuring a basket
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
