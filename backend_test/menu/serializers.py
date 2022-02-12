from rest_framework import generics
from .models import Menu
from .models import MenuOptions
from rest_framework.serializers import ModelSerializer

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id','uuid','date_menu')

class MenuOptionsSerializer(ModelSerializer):
    class Meta:
        model = MenuOptions
        fields = ('menu','option','description')

    def create(self, validated_data):
        option = MenuOptions.objects.create(**validated_data)
        return option

    def update(self, instance, validated_data):
        instance.option = validated_data.get('option',instance.option)
        instance.description= validated_data.get('description',
                                         instance.description)
        instance.save()
        return instance
