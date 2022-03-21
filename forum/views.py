

# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import PostForm
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

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    """
    A view to show individual post
   
    Args:
        DetailView: class based view
    Returns:
        Render of post detail with context
    """
    model = Post
    template_name = "forum/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        post = get_object_or_404(Post, pk=pk)

        context["post"] = post
    
        return context
    
@login_required
def add_post(request, topic):
    """
    A view to add a post, redirects to the post when submitted
    Args:
        request (object): HTTP request object.
        topic: topic
    Returns:
        Render of post form with context
    """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, only logged in users can create a post.')
        return redirect(reverse('home'))
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        topic_obj = get_object_or_404(Topic, name=topic)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(request.POST["title"])
            post.owner = request.user
            post.user_name = request.user.username
            post.topic = topic_obj
            post.post_image = request.FILES.get("post_image")
            post.owner = request.user
            post.save()
            messages.success(request, 'Post submitted')
            return redirect(reverse("postdetail", args=[post.id]))
    context = {"form": form, "topic": topic}
    return render(request, "forum/postform.html", context)


@method_decorator(login_required, name='dispatch')
class UpdatePostView(SuccessMessageMixin, UpdateView):
    """
    A view to edit a post
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        UpdateView: class based view
    Returns:
        Render of update post with success message
    """
    model = Post
    form_class = PostForm
    template_name = "forum/update_post.html"
    success_message = "Post updated"
   

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(owner=owner)
    
@method_decorator(login_required, name='dispatch')
class DeletePostView(SuccessMessageMixin, DeleteView):
    """
    A view to delete a post
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        DeleteView: class based view
    Returns:
        Render of delete post with success message
    """
    model = Post
    template_name = "forum/delete_post.html"
    success_url = reverse_lazy("forum")
    success_message = "Post deleted"