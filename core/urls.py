from django.contrib import admin
from django.urls import path,include
import core
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
]