from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('roomallotment/', views.room_allotment, name='room_allotment'),
]