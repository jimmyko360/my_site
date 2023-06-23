from django.shortcuts import render
import datetime
from django.http import Http404

posts = [
    {
        "title": "my first post",
        "slug": "my-first-post",
        "body": "wassup chat",
        "date": datetime.datetime(2023, 3, 1)
    },
    {
        "title": "my second post",
        "slug": "my-second-post",
        "body": "its ya boi jkizzle",
        "date": datetime.datetime(2023, 4, 1)
    },
    {
        "title": "my third post",
        "slug": "my-third-post",
        "body": "live on twitch.tv",
        "date": datetime.datetime(2023, 5, 1)
    },
]

def post_by_title(request, slug):
  try:
    blog_post = {}

    for post in posts:
      if slug == post["slug"]:
        blog_post = post

    # if you want pass multiple values to the template, you should break them up into separate dict properties here because you can't use key-value pair references in template interpolation
    return render(request, "blog/blog_post.html", {"title": blog_post["title"], "body": blog_post["body"]})
  except:
    raise Http404()

def all_posts(request):
  titles = []

  for post in posts:
    titles.append(post["title"])

  return render(request, "blog/posts.html", {"titles": titles})