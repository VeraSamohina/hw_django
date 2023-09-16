from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Article
from blog.service import send_congratulation


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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()

        if self.object.count_view == 100:
            send_congratulation(self.object.pk)
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body', 'preview')

    def get_success_url(self):
        return reverse('blog:article_view', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog')


def toggle_published(request, pk):
    article_item = get_object_or_404(Article, pk=pk)
    if article_item.is_published:
        article_item.is_published = False
    else:
        article_item.is_published = True
    article_item.save()

    return redirect(reverse('blog:blog'))
