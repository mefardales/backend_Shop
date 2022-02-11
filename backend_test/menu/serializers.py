from rest_framework import generics
from .models import Menu
from .models import MenuOptions

class MenuSerializer(generics.ListCreateAPIView):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuOptionsSerializer(generics.ListCreateAPIView):
    class Meta:
        model = MenuOptions
        fields = '__all__'

