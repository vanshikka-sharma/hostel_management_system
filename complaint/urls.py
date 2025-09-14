from django.urls import path
from . import views

urlpatterns = [
    path('', views.complaint_submit, name='complaint_submit'),
    path('status/', views.complaint_status, name='complaint_status'),
]