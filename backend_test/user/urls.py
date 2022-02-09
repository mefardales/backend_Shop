from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createUser, name='create'),
    path('list', views.listUser, name='list'),
]
