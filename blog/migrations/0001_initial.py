# Generated by Django 4.2.4 on 2023-09-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='статья')),
                ('slug', models.CharField(verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержание')),
                ('preview', models.ImageField(upload_to='previews/', verbose_name='превью')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='не опубликовано')),
                ('count_view', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
