from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',
          views.forum,
          name='forum'),
     path("room/<topic>/",
          views.PostListView.as_view(),
          name="topic"),
     
]
