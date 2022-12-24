from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post 
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
#    return render(request, "home.html", {})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-id"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "addpost.html"
    #fields = ["title", "body"]

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "updatepost.html"
    #fields = ["title", "body"]

class DeletePostView(DeleteView):
    model = Post
    template_name = "deletepost.html"
    success_url = reverse_lazy("home")