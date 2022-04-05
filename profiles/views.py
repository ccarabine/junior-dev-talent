# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from checkout.models import Order
from .models import UserProfile, Skill
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display the user's order history. """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def profile_type(request):
    """ User to select either user or employer status. """
    profiles = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profiles)
        if form.is_valid():
            form.save()
            if 'hiring_manager' in request.POST:
                messages.success(request, 'Profile updated successfully')
                return redirect("talent_center")

    form = UserProfileForm(instance=profiles)

    template = 'profiles/register_user_type.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def talent_center(request):
    """ Display talent center, list profiles by search query """
    """ Using distinct to get only one instance of each user """
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = UserProfile.objects.distinct().filter(
        Q(default_full_name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    context = {'profiles': profiles, 'skills': skills}
    return render(request, 'profiles/talent-center.html', context)


def talent_center_detail(request, pk):
    """ Display talent center detail profile. """
    profiles = UserProfile.objects.get(id=pk)

    skills = profiles.skill_set.exclude(name__exact="")

    context = {'profile': profiles, 'skills': skills}
    return render(request, 'profiles/talent_center_detail.html', context)
