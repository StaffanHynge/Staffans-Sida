from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Mix


class MixView(TemplateView):
    template_name = 'mix/mix.html'  # Specify the template file name

    PRICING = {
        (1, 0): 10,  # Price for 1-5 days and 0-50 stems
        (1, 1): 15,  # Price for 1-5 days and 50-100 stems
        (2, 0): 20,  # Price for 6-10 days and 0-50 stems
        (2, 1): 25,  # Price for 6-10 days and 50-100 stems
        (3, 0): 30,  # Price for 11-15 days and 0-50 stems
        (3, 1): 35,  # Price for 11-15 days and 50-100 stems
    }

    def post(self, request):
        num_stems = request.POST.get('num_stems')
        num_days = request.POST.get('num_days')

        # Process the values as needed
        price = PRICING.get((num_days, num_stems), 0)

        mixes = Mix.objects.all()
        context = {'mixes': mixes, 'price': price}
        return render(request, self.template_name, context)

    def get(self, request):
        mixes = Mix.objects.all()
        context = {'mixes': mixes}
        return render(request, self.template_name, context)
