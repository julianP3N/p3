"""p2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from p2.vista import metodo1
from p2.vista import metodo2
from p2.vista import metodo3
from p2.vista import metodo4


urlpatterns = [
    path('admin/', admin.site.urls),
    path('metodo1/', metodo1),
    path('metodo2/', metodo2),
    path('metodo3/', metodo3),
    path('metodo4/', metodo4), 
]
