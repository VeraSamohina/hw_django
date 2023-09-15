from django import template
from django.conf import settings
register = template.Library()


@register.filter
def media_url(value):
    media_root = settings.MEDIA_URL
    if value:
        return f"{media_root}{value}"
    else:
        return f"{media_root}/photo/black-box.jpg"


@register.simple_tag()
def mediafile(value):
    return f'/media/{value}'
