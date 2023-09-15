

from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('create/', ArticleCreateView.as_view(), name='create'),
]
