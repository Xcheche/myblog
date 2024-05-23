from django.urls import path
from . import views

app_name = "blog"  # Defined the app_name for namespacing

urlpatterns = [
    path(
        "", views.post_list, name="post_list"
    ),  # Correctly mapped the post_list view to the root URL
    path(
        "<int:id>/", views.post_detail, name="post_detail"
    ),  # Correctly mapped the post_detail view to the detail URL
]
