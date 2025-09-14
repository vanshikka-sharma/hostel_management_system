from django.urls import path
from . import views

urlpatterns = [
    path("", views.mark_attendance, name="mark_attendance"),
    path("view", views.view_attendance, name="view_attendance"),
]


