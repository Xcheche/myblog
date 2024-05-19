from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Added a user model


# Create your models here.
class Post(models.Model):
    # Added a status field below
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
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

    class Meta:  # Defining a default sort order
        ordering = ["-publish"]
        indexes = [  # Added a database index
            models.Index(fields=["-publish"]),
        ]

    def __str__(self): # Added a string representation
        return self.title
