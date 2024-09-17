# hello/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.is_christmas, name='is_christmas'),
    path('is_christmas/', views.is_christmas, name='is_christmas'),
    path('secret_santa/', views.secret_santa, name='secret_santa'),
]
