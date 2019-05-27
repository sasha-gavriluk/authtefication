from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Article

class ArticleList(ListView):
    model = Article
    template_name = "article/list.html"

class ArticleDetail(DeleteView):
    model = Article
    template_name = "article/detail.html"

class ArticleUpdate(UpdateView):
    model = Article
    fields = ["title", "body",]
    template_name = "article/edit.html"

class ArticleDelete(DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy('list')

class ArticleCreate(CreateView):
    model = Article
    fields = ["title", "body", "author"]
    template_name = "article/create.html"