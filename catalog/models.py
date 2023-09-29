from django.db import models
from django.db.models import UniqueConstraint, Q

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    @property
    def active_version(self):
        return self.version_set.get(is_active=True)

    title = models.CharField(max_length=400, unique=True, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='photo/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания', )
    date_last_change = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'pk: {self.title}({self.price}, {self.category})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    version_number = models.SmallIntegerField(verbose_name='номер версии')
    version_title = models.CharField(max_length=250, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='активна')

    def __str__(self):
        return f"{self.version_title}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        constraints = (
            UniqueConstraint(fields=['product'], condition=Q(is_active=True), name='unique_active_version',
                             violation_error_message="Может быть только одна активная версия продукта"),
        )
