from blog.models import Article
from django.core.mail import send_mail
from config import settings


def send_congratulation(article_id):
    article_item = Article.objects.get(pk=article_id)
    send_mail('Поздравления', f'Поздравляем!!! /Ваша статья "{article_item.title}" набрала 100 просмотров',
              settings.EMAIL_HOST_USER, ['samohinavera44@gmail.com'])
