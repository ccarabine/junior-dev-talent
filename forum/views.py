# pylint: disable=missing-module-docstring
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, UpdateView, \
    DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import PostForm, CommentForm, TopicForm
from .models import Topic, Post, Comment


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
        page = self.request.GET.get("page")
        paginator = Paginator(self.object.comment_post.all(), 3)
        pk = self.kwargs["pk"]
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = self.object.comment_post.all()
        comment = Comment.objects.filter(owner=self.request.user)
        context["page"] = page
        context["paginator"] = paginator
        context["object_list"] = context["paginator"].get_page(context["page"])
        context["page_obj"] = paginator.get_page(page)
        context["post"] = post
        context["comments"] = comments
        context["comment"] = comment
        context["form"] = form
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


@method_decorator(login_required, name='dispatch')
class AddCommentView(SuccessMessageMixin, CreateView):
    """
    A view to add a comment
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        CreateView: class based view
    Returns:
        Render of comment form with success message and context
    """
    model = Comment
    form_class = CommentForm
    template_name = "forum/commentform.html"
    success_message = "Comment added"

    def form_valid(self, form):
        """
        Set the post id and name to self instances
        Returns form
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
        form.instance.post_id = self.kwargs["pk"]
        form.instance.name = self.request.user.username
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Gets the post, returns context
        Args:
            self (object): Self object
            **kwargs: **kwargs
        Returns:
            Context
        """
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        kwargs["post"] = post
        return super().get_context_data(**kwargs)


@method_decorator(login_required, name='dispatch')
class UpdateCommentView(SuccessMessageMixin, UpdateView):
    """
    A view to edit a comment
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        UpdateView: class based view
    Returns:
        Render of update comment with success message
    """
    model = Comment
    form_class = CommentForm
    template_name = "forum/update_comment.html"
    success_message = "Comment updated"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(owner=owner.id)


@method_decorator(login_required, name='dispatch')
class DeleteCommentView(SuccessMessageMixin, DeleteView):
    """
    A view to delete a comment
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        DeleteView: class based view
    Returns:
        Render of delete comment with success message
    """
    model = Comment
    template_name = "forum/delete_comment.html"
    success_url = reverse_lazy("forum")
    success_message = "Comment deleted"


@login_required
def create_topic(request):
    """
    Use the create form using the post request
    Add the topic
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only logged in users can create a topic.')
        return redirect(reverse('forum'))
    form = TopicForm()

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.topic_image = request.FILES.get("topic_image")
            topic.slug = slugify(request.POST["name"])
            topic.save()
            messages.success(request, 'Topic was added successfully')
            return redirect('forum')
    title = 'Create'

    template = 'forum/topic_form.html'

    context = {
        'form': form,
        'title': title
        }

    return render(request, template, context)


@login_required
def update_topic(request, pk):
    """
    Use the Topic form using the post request
    Get the topic by pk and update the topic
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only logged in users can update a topic.')
        return redirect(reverse('forum'))

    topic = get_object_or_404(Topic, pk=pk)
    form = TopicForm(instance=topic)

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES, instance=topic)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.slug = slugify(request.POST["name"])
            form.save()
            messages.success(request, 'Topic was updated successfully')
            return redirect('forum')

    title = 'Update'

    template = 'forum/topic_form.html'

    context = {
        'form': form,
        'title': title
        }

    return render(request, template, context)


@login_required
def delete_topic(request, pk):
    """ Delete topic  """

    topic = get_object_or_404(Topic, pk=pk)

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only logged in users can delete a topic.')
        return redirect(reverse('forum'))

    if request.method == 'POST':
        topic.delete()
        messages.success(request, 'Topic was deleted successfully')
        return redirect('forum')

    template = 'forum/delete_topic.html'

    context = {
        'topic': topic
        }
    return render(request, template, context)
