

from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_view'),
    path('article/edit/<int:pk>', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete')
]
