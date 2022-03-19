# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Admin class for the topic model.
    """
  
    list_display = (
        "name",
        "friendly_name"
        )
    search_fields = (
        "name",
        )