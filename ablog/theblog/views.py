from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.


# def home(request):
#     context = {}
#     return render(request, "home.html", context)


class HomeView(ListView):
    model = Post
    template_name = "home.html"


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
