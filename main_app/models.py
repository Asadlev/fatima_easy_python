from django.db import models

class Method(models.Model):
    title = models.CharField(max_length=50, verbose_name='Загаловок метода')
    name = models.CharField(max_length=95, verbose_name='Название метода')
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=10000, verbose_name = 'Главный текст')
    description = models.TextField(verbose_name='Длинный текст', max_length=10000)
    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=10000, verbose_name = 'Главный2 текст')
    description = models.TextField(verbose_name='Длинный2 текст', max_length=10000)
    def __str__(self):
        return self.title

class Names(models.Model):
    title = models.CharField(max_length=10000, verbose_name = 'Главный2 текст')
    description = models.TextField(verbose_name='Длинный2 текст', max_length=10000)
    def __str__(self):
        return self.title


