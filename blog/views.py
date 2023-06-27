from django.shortcuts import render
from django.http import Http404
from data import posts
# you don't have to navigate to the data file with ..'s, weird

def post_by_title(request, slug):
  # key-value reference MUST use bracket notation in this file for some reason, e.g. in this view and the all_posts view
  try:
    title = slug.replace("-", " ")
    identified_post = next(post for post in posts if title == post["title"])

    # next() is a python function that basically does the same thing that I was doing before
    # define a variable outside of the scope of the for loop
    # loop through the list and assign the value that you're looking for to that variable

    return render(request, "blog/blog_post.html", {"blog_post": identified_post, "slug": slug})
  except:
    raise Http404()


def post_date(post):
  return post.get("date")
  # use .get() here because it will fail gracefully if there is no "date" rather than crashing

def all_posts(request):
  try:
    sorted_posts = sorted(posts, key=post_date, reverse=True)

    previews = []

    for post in sorted_posts:
      slug = post["title"].replace(" ", "-")

      previews.append({
        "title": post["title"],
        "slug": slug,
      })

    return render(request, "blog/posts.html", {"titles": previews})
  except:
    raise Http404()
