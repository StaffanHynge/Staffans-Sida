from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import BookMix
from .forms import MixForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AddMix(LoginRequiredMixin, CreateView):
    template_name = 'booking/add_mix.html'
    model = BookMix
    form_class = MixForm
    success_url = '/booking/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddMix, self).form_valid(form)

class MixList(ListView): 
    template_name = 'booking/mixlist.html'
    model = BookMix
    context_object_name = 'mixes'

