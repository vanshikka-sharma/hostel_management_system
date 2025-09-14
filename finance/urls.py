from django.urls import path
from . import views

urlpatterns = [
    path('inventoryExpenditure', views.inventoryExpenditure, name='inventoryExpenditure'),
    path('salaryPayments', views.salaryPayments, name='salaryPayments'),
]