# project_name/urls.py
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculator, name='calculator'),
]
