# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin


# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for the product model.
    """
   
    list_display = (
        "category",
        "name",
        "description",
        "price",
        "rating"
        )
    search_fields = (
        "name",
        "description"
        )

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