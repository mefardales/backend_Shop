from django.urls import path
from . import views

urlpatterns = [
    path ('', views.listMenu, name='listMenu'),
    path('create/<int:user_id>', views.createMenu, name='createMenu'),
    path('create/menuoptions/<int:user_id>', views.createMenuOptions, name='createMenuOptions'),
    path('<uuid:uuid>', views.getMenu, name='getMenu'),
    path('update/menuoptions/<int:user_id>', views.updateMenuOptions, name='updateMenuOptions'),
]
