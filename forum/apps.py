# pylint: disable=missing-module-docstring
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig

# Internal:


class ForumConfig(AppConfig):
    """
    A class for the forum configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
