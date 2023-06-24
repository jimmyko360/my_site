from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from data import posts

def index(request):
  # using a try/except block here was causing an error, why?
  # it's because I was returning Http404 instead of raising it
  try:
    return render(request, "homepage/index.html", {"blog_post": posts[0]})
  except:
    raise Http404()