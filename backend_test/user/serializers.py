from rest_framework import generics
from .models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email')

    def validate(self, data):
        if 'username' not in data:
            raise ValidationError({
                'Error username cannot be empty'
            })
        return data

    def create(self, v_data):
        user = User.objects.create(
            name=v_data['name'],
            username=v_data['username'],
            email=v_data['email'])
        return user
