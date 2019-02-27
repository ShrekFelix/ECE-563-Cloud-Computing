from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trial', views.index_trial, name='index_trial'),
    path('query/', views.query, name='query'),
    path('insert/', views.insert, name='insert')
]