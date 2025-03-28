from django.db import models


class Method(models.Model):
    title = models.CharField(max_length=50, verbose_name='Загаловок метода')
    name = models.CharField(max_length=95, verbose_name='Название метода')
    description = models.TextField(default='', verbose_name='Описание метода')
    example_code_image = models.ImageField(upload_to='code_images/', verbose_name='Изображение примера кода', default='')

    def __str__(self):
        return self.name



