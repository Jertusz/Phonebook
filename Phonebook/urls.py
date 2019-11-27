"""Phonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from phonebook_app.views import *


urlpatterns = [
    path('phonebook_app/', include('phonebook_app.urls')),
    path('', OsobaIndexView.as_view(), name='list'),
    path('search/', SearchView.as_view(), name='search'),
    path('<int:pk>/detail/', OsobaDetailView.as_view(), name='people_detail'),
    path('create/', OsobaCreateView.as_view(), name='create'),
    path('<int:pk>/update/', OsobaUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', OsobaDeleteView.as_view(), name='delete'),
    path('<int:pk>/createtel/', TelefonFormView.as_view(), name='createtel'),
    path('<int:pk>/createmail/', EmailFormView.as_view(), name='createmail'),
    #    path('admin/', admin.site.urls),
]
