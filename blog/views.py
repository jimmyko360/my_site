from django.shortcuts import render
from django.http import Http404
from data import posts
# you don't have to navigate to the data file with ..'s, weird

def post_by_title(request, slug):
  blog_post = None

  # key-value reference MUST use bracket notation in this file for some reason, e.g. in this view and the all_posts view
  for post in posts:
    if slug == post["slug"]:
      blog_post = post
  if blog_post:
    return render(request, "blog/blog_post.html", {"blog_post": blog_post})
  else:
    raise Http404()

def all_posts(request):
  try:
    titles = []

    for post in posts:
      titles.append({
        "title": post["title"],
        "slug": post["slug"],
      })

    return render(request, "blog/posts.html", {"titles": titles})
  except:
    raise Http404()
