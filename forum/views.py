

# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from .models import Topic, Post


def forum(request):
    """
    View all topics posts
    """
    topics = Topic.objects.all()
    template = 'forum/forum.html'
    context = {
        'topics': topics
    }
    return render(request, template, context)

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    """
    A view to show 5 lastest posts filtered by topic
    Args:
        ListView: class based view
    Returns:
        Render of post list with context
    """
    template_name = "post_list.html"
    context_object_name = "post_list"
    paginate_by = 6

    def get_queryset(self):  # get all the posts by topic
        queryset = Post.objects.filter(topic__slug=self.kwargs["topic"])
        return queryset

    def get_context_data(self, **kwargs):  # to get the topic selected
        context = super().get_context_data(**kwargs)
        context["topic"] = Topic.objects.get(slug=self.kwargs["topic"])
        return context

