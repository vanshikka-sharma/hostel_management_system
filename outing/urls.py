
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_outing, name='apply_outing'),
    path('add/', views.apply_outing, name='outing_add'),
    path('list/', views.outing_list, name='outing_list'),
]