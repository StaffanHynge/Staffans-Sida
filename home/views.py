<<<<<<< HEAD
from django.shortcuts import render
=======
>>>>>>> 061eb9a2b172138ee6cdf86e3e042976cf815101
from django.views.generic import TemplateView


class Home(TemplateView): 
    template_name = 'home/home.html'
