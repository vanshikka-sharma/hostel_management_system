"""
URL configuration for hostel_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('hostel/', include('hostel.urls')),
    path('finance/', include('finance.urls')),
    path('application/', include('application.urls')),
    path('attendence/', include('attendence.urls')),
    path('complaint/', include('complaint.urls')),
    path('hostel/', include('hostel.urls')),
    path('event/', include('event.urls')),
    path('voting/', include('voting.urls')),
    path('visitors/', include('visitors.urls')),
    path('parcel/', include('parcel.urls')),
    path('inventory/', include('inventory.urls')),
    path('outing/', include('outing.urls')),
    path('notice/', include('notice.urls')),
    path('Mess/', include('Mess.urls')),
    path('staff/', include('staff.urls')),
]
