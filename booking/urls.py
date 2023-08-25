from django.urls import path
from .views import AddMix

urlpatterns = [
    path('', AddMix.as_view(), name='add_mix'),
    # ...
]
