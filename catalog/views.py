from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Магазин хороших товаров',
        'description': 'Предлагаем различные товары по привлекательным ценам'}
    return render(request, 'catalog/homepage.html', context)


def contacts(request):
    context = {'title': 'Наши контакты'}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new feedback from {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html', context)
