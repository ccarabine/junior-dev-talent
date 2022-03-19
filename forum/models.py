# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Topic(models.Model):
    """
    A class for the topic model
    """
    name = models.CharField(
        verbose_name=("name"),
        max_length=100
        )
    friendly_name = models.CharField(
        verbose_name=("friendly_name"),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        )
    topic_image = models.ImageField(
        verbose_name=("topic_image"),
        null=True,
        blank=False,
        upload_to=""
    )

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ['name']
        
    def __str__(self):
        """
        Returns the topic name string
        Args:
            self (object): self.
        Returns:
            The topic name string
        """
        return str(self.name)
    
    def get_friendly_name(self):
        """
        Returns the friendly name string
        Args:
            self (object): self.
        Returns:
            The friendly name name string
        """
        return self.friendly_name
