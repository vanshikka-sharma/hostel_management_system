from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('submit', views.submit, name='submit'),
    path('status', views.status, name='status'),
]