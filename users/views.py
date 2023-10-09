import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from config import settings
from users.models import User
from users.forms import UserRegisterForm, UserForm


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    extra_context = {'title': 'Регистрация нового пользователя'}
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        text_message = ("Вы успешно зарегистрированы на сайте Магазина Хороших товаров. "
                        "Для подтверждения электронной почты перейдите пожалуйста по ссылке")
        id = self.object.id
        url = f"{self.request.build_absolute_uri('verification')}/{id}"
        send_mail(
            subject='Вы зарегистрированы',
            message=f'{text_message} {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
            fail_silently=False
        )
        return super().form_valid(form)


class VerificationView(TemplateView):
    template_name = 'users/verification.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.get(pk=pk)
        user.is_verified = True
        user.save()
        return super(VerificationView, self).get(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    extra_context = {'title': 'Редактирование профиля'}
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    new_password = ''.join([str(random.randint(0,9)) for _ in range(10)])
    send_mail(
        subject='Вы успешно сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('catalog:home'))
