# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import OrderForm


def checkout(request):
    """
    Checkout for the user
    Args:
        request (object): Request object
    Returns:
        Render of checkout
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
