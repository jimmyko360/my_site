from django.shortcuts import render
from django.http import Http404
from data import posts
# you don't have to navigate to the data file with ..'s, weird

def post_by_title(request, slug):
  blog_post = None

  # key-value reference MUST use bracket notation in this file for some reason, e.g. in this view and the all_posts view
  for post in posts:
    title = slug.replace("-", " ")

    if title == post["title"]:
      blog_post = post
    # ^this process will be very inefficient if you have a lot of posts
  if blog_post:
    return render(request, "blog/blog_post.html", {"blog_post": blog_post, "slug": slug})
  else:
    raise Http404()

def all_posts(request):
  try:
    titles = []

    for post in posts:
      slug = post["title"].replace(" ", "-")

      titles.append({
        "title": post["title"],
        "slug": slug,
      })

    return render(request, "blog/posts.html", {"titles": titles})
  except:
    raise Http404()
