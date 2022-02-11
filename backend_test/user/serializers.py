from rest_framework import generics
from .models import User


class UserSerializer(generics.ListCreateAPIView):
    class Meta:
        model = User
        fields = '__all__'


