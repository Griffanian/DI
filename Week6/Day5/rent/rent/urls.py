"""
URL configuration for rent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental/',views.show_all_rentals),
    path('rent/rental/<int:pk>',views.show_1_rental),
    path('rent/rental/add',views.new_rental),
    path('rent/customer/<int:pk>',views.show_1_customer),
    path('rent/customer/',views.show_all_customers),
    path('rent/customer/add',views.new_customer),
    path('rent/vehicle/',views.show_all_vehicles),
    path('rent/vehicle/<int:pk>',views.show_1_vehicle),
    path('rent/vehicle/add',views.new_vehicle),
]
