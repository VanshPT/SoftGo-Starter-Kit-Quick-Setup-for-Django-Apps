from django.urls import path,include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('login/', views.login_page_render, name="login_page_render"),
    path('register/', views.register_page_render, name="register_page_render"),
    path('register_user/', views.register, name='register'),
    path('login_user/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]