# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views

urlpatterns = [
    path(
        '',
        views.profile,
        name='profile'
        ),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
        ),
    path(
        'profile_type',
        views.profile_type,
        name='profile_type'
        ),
    path(
        'talent_center',
        views.talent_center,
        name='talent_center'
        ),
    path('talent_center_detail/<str:pk>/',
         views.talent_center_detail,
         name="talent_center_detail"),
]
