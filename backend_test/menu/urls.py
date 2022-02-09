from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createMenu, name='create'),
    path('create/menuoptions/', views.createMenuOptions, name='create'),
    path('update/menuoptions/<str:pk>', views.updateMenuOptions, name='update'),
]
