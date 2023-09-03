from django.shortcuts import render


def home(request):
    return render(request, 'catalog/homepage.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new feedback from {name}({phone}): {message}')

    return render(request, 'catalog/contacts.html')
