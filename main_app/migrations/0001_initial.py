# Generated by Django 5.1.7 on 2025-03-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Загаловок метода')),
                ('name', models.CharField(max_length=25, verbose_name='Название метода')),
                ('description', models.TextField(verbose_name='Загаловок метода')),
                ('example_code_image', models.ImageField(upload_to='method_images/', verbose_name='Изображение кода')),
            ],
        ),
    ]
