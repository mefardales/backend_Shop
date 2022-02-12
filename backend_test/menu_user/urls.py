from django.urls import path
from .views import UserMenuAPIView as views

urlpatterns = [
    path('list/<int:user_id>', views.getOrder, name='getOrder'),
    path('<int:user_id>', views.createOrder, name='createOrder'),
]
