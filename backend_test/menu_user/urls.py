from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/list', views.getOrder, name='getOrder'),
    path('<int:user_id>', views.createOrder, name='createOrder'),
]
