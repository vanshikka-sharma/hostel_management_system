from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('add', views.add, name='add'),

]