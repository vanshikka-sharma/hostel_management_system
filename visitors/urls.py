
from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_visitor, name='record_visitor'),
    path('success/', views.visitor_success, name='visitor_success'),
    path('', views.history, name='visitor_history'),
]