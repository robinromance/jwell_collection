from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('service/', views.service, name = 'service'),
    path('news/', views.news, name = 'news'),
    path('mail/', views.mail, name = 'mail'),
    path('single/', views.single, name = 'single'),
]
