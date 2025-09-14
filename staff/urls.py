from django.urls import path
from . import views

urlpatterns = [
    path("", views.staff_home, name="staff_home"),
    path("add/", views.add_member, name="add_member"),
    path("shift/<int:pk>/", views.shift_member, name="shift_member"),
]
