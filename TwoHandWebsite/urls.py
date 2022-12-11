"""TwoHandWebsite URL Configuration

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
from app01 import views
from TwoHandWebsite.settings import MEDIA_ROOT
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.marketfront),
    path('login/', views.login),
    path('upload/', views.upload),
    path('mainpage/', views.mainpage),
    path('marketfront/', views.marketfront),
    path('loadposts/', views.loadposts),
    path('profile/', views.profile)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
