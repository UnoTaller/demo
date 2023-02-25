from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
]
