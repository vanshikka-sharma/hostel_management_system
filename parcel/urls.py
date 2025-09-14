from django.urls import path
from . import views

app_name = 'parcel'

urlpatterns = [
    path('', views.base, name='base'),
    path('send/', views.send_parcel, name='send_parcel'),
    path('history/', views.history, name='history'),
]