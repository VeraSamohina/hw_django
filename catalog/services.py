from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_cached_products():
    if settings.CACHE_ENABLE:
        key = 'product_list'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.all()[:6]
            cache.set(key, product_list)
            return product_list
        return product_list
