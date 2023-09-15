from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='статья')
    slug = models.CharField(verbose_name='slug')
    body = models.TextField(verbose_name='содержание')
    preview = models.ImageField(upload_to='previews/', verbose_name='превью')
    date_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='не опубликовано')
    count_view = models.IntegerField(default=0, verbose_name='количество просмотров')

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.title
