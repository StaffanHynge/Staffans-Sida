from django.urls import path
from .views import Home, aryan
from . import views


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('aryan/', views.aryan, name='aryan'),
]
