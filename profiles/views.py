# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from checkout.models import Order
from util.util import pagination_setup
from .models import UserProfile, Skill
from .forms import UserProfileForm, UserAccountForm, SkillForm


@login_required
def edit_profile(request):
    """ Display the user's profile with instance and update """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("display_profile")
        else:
            messages.error(request, 'Failed to update profile. Please ensure the form is valid.')
    else:
       
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)


@login_required
def edit_account(request):
    """ Display the user's profile account information. """
    account_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect("account_details")

    form = UserAccountForm(instance=account_profile)

    template = 'profiles/edit_account.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
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

@login_required
def register_hiring_manager(request):
    """ When this function is called, it registers the user as a hiring manager. """
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.is_hiring_manager = True
    profile.save()
    messages.success(request, 'Successfully registered as a hiring manager')
    return redirect(talent_center)


@login_required
def profile_type(request):
    """ Render the register user type template. """

    template = 'profiles/register_user_type.html'

    return render(request, template)

 
@login_required
def talent_center(request):
    """ Display talent center, list profiles by search query """
    """ Using distinct to get only one instance of each user """
    """ Paginate by 6 """
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = UserProfile.objects.distinct().filter(
        Q(default_full_name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    profiles = pagination_setup(profiles, request, 6)

    context = {'profiles': profiles, 'skills': skills}
    return render(request, 'profiles/talent-center.html', context)


@login_required
def talent_center_detail(request, pk):
    """ Display talent center detail profile. """
    profiles = UserProfile.objects.get(id=pk)

    skills = profiles.skill_set.exclude(name__exact="")

    context = {'profile': profiles, 'skills': skills}
    return render(request, 'profiles/talent_center_detail.html', context)


@login_required
def contact_developer(request, pk):
    """
    Sends email -contact us form fields to admin or prints to the terminal
    in development
    Prepopulates email and username
    Args:
       request (object): HTTP request object.
       slug: slug
    Returns:
       Render contact us page  with context
    """
    profile = get_object_or_404(UserProfile, pk=pk)

    if profile.default_email:
        if request.method == "POST":
            message_subject = request.POST['message-subject']
            developer_email = profile.default_email
            message_body = request.POST['message']
            send_mail(
                message_subject,
                message_body,
                'projectckcabs@gmail.com',
                [developer_email],
            )
            messages.success(request, 'Email sent successfully')
            return redirect("talent_center")
    else:
        messages.error(
            request,
            'Candidate does not have an email address unfortunately')
        return redirect("talent_center")
    return render(request, 'profiles/contact.html', {'profile': profile})


@login_required
def display_profile(request):
    """ Display the user's personal profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    skills = profile.skill_set.all()

    template = 'profiles/display_profile.html'
    context = {
        'on_profile_page': True,
        'profile': profile,
        'skills': skills
        }
    return render(request, template, context)


@login_required
def account_details(request):
    """ Display the user's billing details and order. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/account_details.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
        'profile': profile,
        }

    return render(request, template, context)

@login_required
def subscription(request):
    """ Render the subscription template. """

    template = 'profiles/subscription.html'

    return render(request, template)

@login_required
def create_skill(request):
    """ Use the skill form using the post request """
    """ Add the skill for the particular owner to their """
    """ profile """
    
    profile = request.user.user_profile
    form = SkillForm()
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully')
            return redirect('display_profile')
    title = 'Create'
    
    template = 'profiles/skill_form.html'

    context = {
        'form': form,
        'title': title
        }

    return render(request, template, context)

@login_required
def update_skill(request, pk):
    """ Use the skill form using the post request """
    """ update the skill for the particular owner to their """
    """ profile """
    
    profile = request.user.user_profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully')
            return redirect('display_profile')
    title = 'Update'
    
    template = 'profiles/skill_form.html'

    context = {
        'form': form,
        'title': title
        }

    return render(request, template, context)

@login_required
def delete_skill(request, pk):
    """ Delete the skill  """
    
    profile = request.user.user_profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully')
        return redirect('display_profile')
    
    template = 'profiles/delete_skill.html'
    
    context = {
        'skill': skill
        }

    return render(request, template, context)
