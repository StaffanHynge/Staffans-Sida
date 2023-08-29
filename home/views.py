
from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView): 
    template_name = 'home/home.html'


def aryan(request):
    return render(request, 'home/aryan.html')
