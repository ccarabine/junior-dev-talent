# pylint: disable=missing-module-docstring
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views

urlpatterns = [
    path(
        'edit_profile',
        views.edit_profile,
        name='edit_profile'
        ),
    path(
        'edit_account',
        views.edit_account,
        name='edit_account'
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
        'register_hiring_manager',
        views.register_hiring_manager,
        name='register_hiring_manager'
        ),
    path(
        'talent_center',
        views.talent_center,
        name='talent_center'
        ),
    path(
         'talent_center_detail/<str:pk>/',
         views.talent_center_detail,
         name="talent_center_detail"
         ),
    path(
         "contact_developer/<str:pk>/",
         views.contact_developer,
         name="contact_developer"
         ),
    path(
         "display_profile",
         views.display_profile,
         name="display_profile"
         ),
    path(
         "account_details",
         views.account_details,
         name="account_details"
         ),
    path(
         "subscription",
         views.subscription,
         name="subscription"
         ),
    path(
         "create_skill",
         views.create_skill,
         name="create_skill"
         ),
    path(
         "update_skill/<str:pk>",
         views.update_skill,
         name="update_skill"
         ),
    path(
         "delete_skill/<str:pk>",
         views.delete_skill,
         name="delete_skill"
         ),
    path(
         "delete_account/<int:pk>",
         views.DeleteAccountView.as_view(),
         name="delete_account"
         ),
]
