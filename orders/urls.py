"""
URL configuration for brocart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from orders import views

urlpatterns = [
    
    path('cart/',views.showcart,name='cart'),
    path('add_cart/',views.add_cart,name='add_cart'),
    path('remove_cart_item/<pk>',views.remove_cart_item,name='remove_cart_item'),
    path('checkout_order/',views.checkout_order,name='checkout_order'),
     path('order_list/',views.order_list,name='order_list'),
]
