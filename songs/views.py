from django.shortcuts import render
from django.views.generic import TemplateView


class Songs(TemplateView):
    template_name = 'songs/songs.html'
