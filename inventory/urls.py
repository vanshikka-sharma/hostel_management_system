from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_main, name='inventory_main'),
    path('add/', views.inventory_add, name='inventory_add'),
    path('usage/', views.inventory_usage, name='inventory_usage'),
]
