from django.shortcuts import render

def forum(request):
    """ A view to return the index page """

    return render(request, 'forum/forum.html')