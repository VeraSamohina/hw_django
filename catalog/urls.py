from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (contacts, ProductListView, ProductDetailView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
          path('', ProductListView.as_view(), name='home'),
          path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
          path('product/', ProductCreateView.as_view(), name='product_create'),
          path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
          path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
          path('contacts/', contacts, name='contacts'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
