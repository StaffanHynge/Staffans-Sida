from django import forms
from .models import BookMix


class MixForm(forms.ModelForm):
    class Meta: 
        model = BookMix
        fields = ['name', 'time', 'stems', 'price' ]

        labels = {
            'name': 'Name',
            'time': 'Time',
            'stems': 'Stems',
            'price': 'Price'
        }
        