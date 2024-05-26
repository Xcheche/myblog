from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Added a user model
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    # Added a status field below
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )  # Added a many-to-one relationship
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Added a status field completion below
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )


# Creating model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    objects = (
        models.Manager()
    )  # The default manager.     published = PublishedManager() # Our custom manager.

    class Meta:  # Defining a default sort order
        ordering = ["-publish"]
        indexes = [  # Added a database index
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):  # Added a string representation
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )
