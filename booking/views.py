from django.shortcuts import render
from django.views.generic import CreateView
from .models import BookMix
from .forms import MixForm


class AddMix(CreateView):
    template_name = 'booking/add_mix.html'
    model = BookMix
    form_class = MixForm
    success_url = '/booking/'

    def form_valid(self, form):
        return super(AddMix, self).form_valid(form)

