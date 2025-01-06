"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('user_login/', user_login),
    path('user_logup/', user_logup),
    path("home/", home),
    path("logout/", user_logout),

    path('main/', main),
    path('main/add_cart/<int:id>', add_cart),
    path('main/remove_cart/<int:id>', remove_cart),
    path('main/clean_cart', clean_cart),
    
    path('main/sale', sale),
    path('main/sales_view', sales_view),
    path('main/sales_view/<int:id>', sale_detail)
]
