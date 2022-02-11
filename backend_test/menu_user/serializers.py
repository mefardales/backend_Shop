from rest_framework import generics
from .models import MenuUser


class MenuUserSerializer(generics.ListCreateAPIView):
    class Meta:
        model = MenuUser
        fields = '__all__'


