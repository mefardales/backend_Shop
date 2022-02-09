from rest_framework import serializers
from .models import MenuUser


class MenuUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuUser
        fields = '__all__'


