# pylint: disable=missing-module-docstring
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Admin class for the product model.
    """

    list_display = (
        "category",
        "name",
        "price",
        "image",
        )
    search_fields = (
        "name",
        "description"
        )
    ordering = ('name',)
    summernote_fields = ('description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for the category model.
    """

    list_display = (
        "name",
        "friendly_name"
        )
    search_fields = (
        "name",
        )
