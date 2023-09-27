

from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    toggle_published

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('article/<slug>', ArticleDetailView.as_view(), name='article_view'),
    path('article/edit/<slug>', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/delete/<slug>', ArticleDeleteView.as_view(), name='article_delete'),
    path('pub/<int:pk>', toggle_published, name='pub')
]
