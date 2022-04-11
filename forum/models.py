# pylint: disable=missing-module-docstring
# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.contrib.auth.models import User
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Topic(models.Model):
    """
    A class for the topic model
    """
    name = models.CharField(
        verbose_name=("name"),
        max_length=100,
        unique=True,
        null=True,
        blank=False,
        )
    friendly_name = models.CharField(
        verbose_name=("friendly_name"),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        )
    slug = models.SlugField(
        verbose_name=("slug"),
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
        """
        Set Verbose name Topic and ordering
        """
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


class Post(models.Model):
    """
    A class for the post model
    """
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
        default=1)
    title = models.CharField(
        verbose_name=("title"),
        max_length=200,
        unique=True
        )
    body = models.TextField(
        verbose_name=("body"),
        blank=True
        )
    user_name = models.CharField(
        verbose_name=("user_name"),
        max_length=200,
        blank=True,
        null=True
        )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="post_owner")
    slug = models.SlugField(
        verbose_name=("slug"),
        max_length=150,
        unique=True
        )
    updated = models.DateTimeField(
        verbose_name=("updated"),
        auto_now=True
        )
    created = models.DateTimeField(
        verbose_name=("created"),
        auto_now_add=True
        )
    post_image = models.ImageField(
        verbose_name=("post_image"),
        null=True,
        blank=True,
        upload_to=""
        )

    class Meta:
        """
        Set Verbose name Post and ordering
        """
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]

    def __str__(self):
        """
        Returns the post name string
        Args:
            self (object): self.
        Returns:
            The post title string
        """
        return str(self.title)

    def get_absolute_url(self):
        """
        Returns the post.pk string
        Args:
            self (object): self.
        Returns:
            The url string topic/post pk
        """
        return f"/forum/topic/{self.pk}"


class Comment(models.Model):
    """
    A class for the comment model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comment_post"
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        default='',
        related_name="comment_owner")
    name = models.CharField(
        verbose_name=("name"),
        max_length=80
        )
    comment_body = models.TextField(
        verbose_name=("comment_body"),
        )
    created = models.DateTimeField(
        verbose_name=("created"),
        auto_now_add=True
        )

    class Meta:
        """
        Set Verbose name Comment and ordering
        """
        ordering = ["created"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        """
        Returns the comment name string
        Args:
            self (object): self.
        Returns:
            The comment body by name string
        """
        return f"Comment {self.comment_body} by {self.name}"

    def get_absolute_url(self):
        """
        Returns the post.id string
        Args:
            self (object): self.
        Returns:
            The url string forum/topic/post id
        """
        return f"/forum/topic/{self.post_id}"
