# pylint: disable=missing-module-docstring
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig

# Internal:


class HomeConfig(AppConfig):
    """
    A class for the Home app
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
