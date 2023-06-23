from django.shortcuts import render
from data import posts

def index(request):
  # using a try/except block here was causing an error, why?
  return render(request, "homepage/index.html", {"blog_post": posts[0]})