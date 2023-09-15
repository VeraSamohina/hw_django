from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:blog')


class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Наши статьи'
    }


class ArticleDetailView(DetailView):
    model = Article

