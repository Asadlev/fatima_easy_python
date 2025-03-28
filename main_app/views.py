from django.shortcuts import render
from django.views.generic import DetailView

from .models import Method



def main(request):
    methods = Method.objects.all()
    context = {
        'methods': methods
    }
    return render(request, 'main_app/main.html', context)



class MethodDetailView(DetailView):
    model = Method
    context_object_name = 'method'
    template_name = 'main_app/detail.html'



def about(request):
    return render(request, 'main_app/about.html')




