from rest_framework import serializers
from .models import Menu
from .models import MenuOptions

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOptions
        fields = '__all__'

