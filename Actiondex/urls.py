from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trial/', views.index_trial, name='index_trial'),
    path('trial/query/', views.query, name='query'),
    path('trial/insert/', views.insert, name='insert')
]