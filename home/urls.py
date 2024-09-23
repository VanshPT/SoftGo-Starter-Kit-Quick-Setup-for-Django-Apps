from django.urls import path,include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('dashboard/<str:username>/', views.render_dashboard, name="render_dashboard")
    
]