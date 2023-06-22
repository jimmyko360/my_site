from django.shortcuts import render
import datetime

posts = [
    {
        "title": "my first post",
        "body": "hooray",
        "date": datetime.datetime(2023, 3, 1)
    },
    {
        "title": "my second post",
        "body": "take two",
        "date": datetime.datetime(2023, 4, 1)
    },
    {
        "title": "my third post",
        "body": "wassup chat",
        "date": datetime.datetime(2023, 5, 1)
    },
]

def all_posts(request):
  titles = []

  for post in posts:
    titles.append(post["title"])

  return render(request, "blog/posts.html", {"titles": titles})