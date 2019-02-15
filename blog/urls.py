from django.urls import path
from . import views  # correct variant

urlpatterns = [
    path("", views.allblogs, name="allblogs"),
    path("<int:blog_id>/", views.detail, name="detail"),  # look for specific id (reminder db creates id field auto)
    # whenever someone looks for specific id it saves it for later use for the func/db
]