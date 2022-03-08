from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]