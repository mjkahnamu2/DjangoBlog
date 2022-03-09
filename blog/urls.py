from unicodedata import name
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('search/', SearchResultsView.as_view(), name='post_search'),
    re_path('(?P<slug>[-\w]+)/', post_detail, name='post_detail'),
]