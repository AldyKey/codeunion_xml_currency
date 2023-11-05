from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_repeat', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_repeat = validated_data.pop('password_repeat')
        if password != password_repeat:
            raise serializers.ValidationError("Passwords do not match.")

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
