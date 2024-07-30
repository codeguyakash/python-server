from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

# Assuming your CustomUser model is the default user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_customer', 'is_channel_partner', 'is_employee')


    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_customer=validated_data.get('is_customer', False),
            is_channel_partner=validated_data.get('is_channel_partner', False),
            is_employee=validated_data.get('is_employee', False)
        )
        return user


