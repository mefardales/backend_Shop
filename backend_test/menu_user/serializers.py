from rest_framework import generics
from .models import MenuUser
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from menu.models import MenuOptions

class MenuUserSerializer(ModelSerializer):
    option = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MenuUser
        fields = (
            'specification',
            'option',
            'menu_option',
            'quantity',
            'order_date',
            'username',
            'user_id',)

    def get_option(self, user_menu):
        menu = MenuOptions.objects.filter(id=user_menu.menu_option.id).first()
        return menu.description
    
    def get_user_id(self, user_menu):
        return user_menu.user.id

    def get_username(self, user_menu):
        return user_menu.user.name

    def validate(self, data):
        if 'menu_option' not in data:
            raise ValidationError(
                {'Error menu option cannot be empty'})
        if 'quantity' not in data:
            raise ValidationError({
                'Error quantity cannot be empty'
            })
        return data

