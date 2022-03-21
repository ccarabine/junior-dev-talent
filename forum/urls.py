from django.contrib import admin
from django.urls import path
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
     
]
