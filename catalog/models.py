from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=400, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='photo/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания', )
    date_last_change = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'pk: {self.title}({self.price}, {self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
