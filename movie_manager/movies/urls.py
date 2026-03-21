"""
URL configuration for movie_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list,name='movie_list'),
    path('create/', views.movie_create,name='movie_create'),
    path('list/<pk>/', views.movie_list,name='movie_list'),
    path('edit/<pk>/', views.movie_edit,name='movie_edit'),
    path('delete/<pk>/', views.movie_delete,name='movie_delete'),
]
