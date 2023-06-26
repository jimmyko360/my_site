from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.post_by_title, name="post_by_title"),
    # it's best to use the slug type enforcer in a URL with a slug
    # BUT this restricts you to letters, numbers, hyphens, and underscores
    # having that apostrophe in my title will break some of the pages
    path("", views.all_posts, name="all_posts")
]