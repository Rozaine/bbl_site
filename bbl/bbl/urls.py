"""
URL configuration for bbl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('phy_sec', views.phy_sec, name='phy_sec'),
    path('video_sec', views.video_sec, name='video_sec'),
    path('radio_sec', views.radio_sec, name='radio_sec'),
    path('cargo_sec', views.cargo_sec, name='cargo_sec'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contacts', views.contacts, name='contacts'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('succsess', views.succsess, name='succsess'),
]
