from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views.generic.edit import UpdateView

from post.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "post/home.html", {"posts": posts})


def about(request):
    return render(request, "post/about.html")


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "posts"


class PostCreateView(CreateView):
    model = Post
    template_name = "post/post_new.html"
    fields = ["title", "body", "author"]
    success_url = reverse_lazy("home")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("home")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post/post_edit.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("home")


