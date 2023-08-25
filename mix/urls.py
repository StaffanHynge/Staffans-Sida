from django.urls import path
from .views import MixView

urlpatterns = [
    path('mix/', MixView.as_view(), name='mix'),
    # ...
]
