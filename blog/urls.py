from django.urls import path
from . import views

urlpatterns = [
    path("<str:slug>", views.post_by_title, name="post_by_title"),
    path("", views.all_posts, name="all_posts")
]