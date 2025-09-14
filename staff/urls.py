# staff/urls.py
from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.base, name='base'),
    path('shift/', views.shift_overview, name='shift'),
    path('add/', views.manage_shifts, name='add'),
    path('salary/', views.salary_overview, name='salary'),
    # extras
    path('staff/add/', views.staff_create, name='staff_add'),
    path('staff/<int:pk>/edit/', views.staff_edit, name='staff_edit'),
]
