
from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_visitor, name='record_visitor'),
    path('', views.history, name='visitor_history'),
]