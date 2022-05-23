# pylint: disable=missing-module-docstring
# # Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views

urlpatterns = [
    path(
        '',
        views.view_basket,
        name='view_basket'
        ),
    path(
        'add/<item_id>/',
        views.add_to_basket,
        name='add_to_basket'
        ),
    path(
        'adjust/<item_id>/',
        views.adjust_basket,
        name='adjust_basket'
        ),
    path(
        'remove/<item_id>/',
        views.remove_from_basket,
        name='remove_from_basket'
        ),
]
