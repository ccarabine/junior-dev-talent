# pylint: disable=missing-module-docstring
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Topic, Post, Comment


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Admin class for the topic model.
    """
    prepopulated_fields = {
        "slug": ("name",),
        }
    list_display = (
        "name",
        "friendly_name"
        )
    search_fields = (
        "name",
        )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class for the post model.
    """
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_display = (
        "title",
        "topic",
        "owner",
        "created"
        )
    search_fields = (
        "title",
        "topic"
        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the comment model.
    """
    list_display = (
        "name",
        "comment_body",
        "post",
        "created"
        )
    search_fields = (
        "name",
        "body"
        )
