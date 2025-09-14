from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.base, name='base'),
    path('add/', views.add, name='add'),
]