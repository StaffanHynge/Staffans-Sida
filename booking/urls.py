from django.urls import path
from .views import AddMix, MixList

urlpatterns = [
    path('', AddMix.as_view(), name='add_mix'),
    path('mixlist/', MixList.as_view(), name='mix_list'),
    # ...
]
