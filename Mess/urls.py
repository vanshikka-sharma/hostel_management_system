from django.urls import path
from . import views

urlpatterns = [
    path('menu',views.menu,name='menu'),
    path('stocks',views.stocks,name='stocks'),
    path('salaryPayments',views.salaryPayments,name='salaryPayments'),
    path('messFees',views.messFees,name='messFees'),

]