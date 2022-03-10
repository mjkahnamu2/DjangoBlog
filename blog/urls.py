from unicodedata import name
from django.views.generic import TemplateView
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('search/', SearchResultsView.as_view(), name='post_search'),
    path('تماس با من/', TemplateView.as_view(template_name='blog/contact.html'), name='contact_me'),
    re_path('(?P<slug>[-\w]+)/', post_detail, name='post_detail'),
]