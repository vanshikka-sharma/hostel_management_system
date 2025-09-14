from django.urls import path
from . import views

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("add/", views.add_item, name="add_item"),
    path("usage/", views.record_usage, name="record_usage"),
]
