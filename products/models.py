# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Category(models.Model):
    """
    A class for the Category model
    """
    name = models.CharField(
        max_length=254
        )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )
    
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self
        Returns:
            The category name string
        """
        return str(self.name)
    
    def get_friendly_name(self):
        """
        Returns the friendly name name string
        Args:
            self (object): self.
        Returns:
            The friendly name string
        """
        return self.friendly_name

class Product(models.Model):
    """
    A class for the Product model
    """
    category = models.ForeignKey(
        'Category', null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(
        max_length=254
        )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
        )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
        )
    image = models.ImageField(
        null=True,
        blank=True
        )

    def __str__(self):
        """
        Returns the Product name string
        Args:
            self (object): self
        Returns:
            The Product name string
        """
        return str(self.name)
