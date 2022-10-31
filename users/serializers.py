from unicodedata import name
from rest_framework import serializers
from students.models import Students
from .models import Users
from parents.serializers import ParentSerializer
# from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        style={'input_type': 'text', 'placeholder': 'email'})
    password = serializers.CharField(
        style={'input_type': 'password', 'placeholder': 'Password'})

    def create(self, validated_data):
        # validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    class Meta:
        model = Users
        fields = ['email', 'password']
