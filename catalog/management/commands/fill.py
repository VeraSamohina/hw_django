import json
from django.core.management import BaseCommand
from catalog.models import Product, Category
from config.settings import BASE_DIR

class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()
        try:
            with open(BASE_DIR/'category.json', 'r', encoding='UTF-8') as f:
                categories = json.load(f)
                for item in categories:
                    Category.objects.create(
                        pk=item['pk'],
                        title=item['fields']['title'],
                        description=item['fields']['description']
                    )
            with open(BASE_DIR/'product.json', 'r', encoding='UTF-8') as f:
                products = json.load(f)
                for item in products:
                    category_pk = item['fields']['category']
                    category = Category.objects.get(pk=category_pk)
                    Product.objects.create(
                        pk=item['pk'],
                        title=item['fields']['title'],
                        description=item['fields']['description'],
                        category=category,
                        price=item['fields']['price'],
                        date_create=item['fields']['date_create'],
                        date_last_change=item['fields']['date_last_change']
                    )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте данных: {e}'))

        else:
            self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных'))
