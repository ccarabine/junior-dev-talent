from django.shortcuts import render

def error_404_view(request, exception):
    """
    A view to render 404 error page if the user goes to a non-exist url
    Args:
        request (object): HTTP request object.
        exception: exception error
    Returns:
        Render 404error page
    """
    return render(request, 'errors/404error.html', status=404)


def error_500_view(request):
    """
    A view to render 500 error page if there is a server error such
    as the api failing
    Args:
        request (object): HTTP request object.
    Returns:
        Render 500error page
    """
    return render(request, 'errors/500error.html', status=500)


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
