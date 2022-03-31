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
        'stripe_public_key': 'pk_test_51KYnn3K0LINE1GrIoKeKr16tN5KSn4w7kO80cIGGwsY1HkdyEbsZSZj4Qh2hsqOnqKFDuO0hWnShj0LTycpC5MPS00Xfw1C6Mw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
