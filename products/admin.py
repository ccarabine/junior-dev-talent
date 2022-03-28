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
        'sku',
        "category",
        "name",
        "description",
        "price",
        "rating",
        "image",
        )
    search_fields = (
        "name",
        "description"
        )
    ordering = ('sku',)

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