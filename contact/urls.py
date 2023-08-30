from django.urls import path
from .views import contact
from . import views

urlpatterns = [

    path('contact/', views.contact, name='contact'),
]
