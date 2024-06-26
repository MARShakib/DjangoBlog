from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, EditForm
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     context = {}
#     return render(request, "home.html", context)


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # # Necessary when use the model only. (commented out as form_class added)
    # fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ["title", "title_tag", "body"]

    # After edit move to the home.
    success_url = reverse_lazy("home")


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"

    success_url = reverse_lazy("home")
