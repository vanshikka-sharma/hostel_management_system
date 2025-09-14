from django.urls import path
from . import views

urlpatterns = [
    path('applyhistory', views.applyhistory, name='applyhistory'),

]