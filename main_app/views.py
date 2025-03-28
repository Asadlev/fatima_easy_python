from django.shortcuts import render
from .models import Method, Names
from .models import Article, Card


def main(request):
    methods = Method.objects.all()
    context = {'methods': methods}
    return render(request, 'main_app/main.html', context)


def about(request):
    names = Names.objects.all()
    context = {'names': names}
    return render(request, 'main_app/about.html', context)

def cart1(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'main_app/cart1.html', context)





