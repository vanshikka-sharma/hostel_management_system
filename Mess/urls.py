from django.urls import path
from . import views

urlpatterns = [
    path("", views.mess_timetable, name="mess_timetable"),
    path("add/", views.add_menu, name="add_menu"),
    path("update/<int:pk>/", views.add_menu, name="update_menu"),
    path('inventory/', views.mess_inventory, name='mess_inventory'),
]
