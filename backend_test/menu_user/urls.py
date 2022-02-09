from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listMenuUser, name='list'),
    path('create', views.createMenuUser, name='create'),
]
