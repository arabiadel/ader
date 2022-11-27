from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Post



class PostHomeView(ListView):
    model = Post
    template_name = "Posts/home.html"


