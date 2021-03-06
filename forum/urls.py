# pylint: disable=missing-module-docstring
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views

urlpatterns = [
     path('',
          views.forum,
          name='forum'),
     path("<topic>/",
          views.PostListView.as_view(),
          name="topic"),
     path("topic/<int:pk>",
          views.PostDetailView.as_view(),
          name="postdetail"),
     path("addpost/<topic>/",
          views.add_post,
          name="addpost"),
     path("update/<int:pk>",
          views.UpdatePostView.as_view(),
          name="updatepost"),
     path("topic/<int:pk>/remove",
          views.DeletePostView.as_view(),
          name="deletepost"),
     path("topic/<int:pk>/comment/",
          views.AddCommentView.as_view(),
          name="addcomment"),
     path("update/comment/<int:pk>",
          views.UpdateCommentView.as_view(),
          name="updatecomment"),
     path("topic/comment/<int:pk>/remove",
          views.DeleteCommentView.as_view(),
          name="deletecomment"),
     path("topic/create_topic",
          views.create_topic,
          name="create_topic"),
     path("topic/update_topic/<int:pk>",
          views.update_topic,
          name="update_topic"),
     path("delete_topic/<str:pk>",
          views.delete_topic,
          name="delete_topic"),
]
