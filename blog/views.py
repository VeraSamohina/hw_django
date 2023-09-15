from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from pytils.translit import slugify

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid:
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)



class ArticleListView(ListView):
    model = Article
    extra_context = {
        'title': 'Наши статьи'
    }


class ArticleDetailView(DetailView):
    model = Article

