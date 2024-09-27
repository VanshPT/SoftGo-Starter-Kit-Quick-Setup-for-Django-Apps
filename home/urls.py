from django.urls import path,include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('dashboard/<str:username>/', views.render_dashboard, name="render_dashboard"),
    path('auto_clustering/<str:username>/', views.auto_clustering, name="auto_clustering"),
    path('explore_topics/<str:username>/', views.explore_topics, name="explore_topics"),
    path('search_papers/<str:username>/', views.search_papers, name="search_papers"),
    
]