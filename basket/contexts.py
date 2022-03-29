# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.conf import settings

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    grand_total = total
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context