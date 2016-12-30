import re

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url',
                  'thumbnail',
                  'telephone',
                  'is_admin',
                  'is_active')


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telephone',
                  'password')

    def validate_telephone(self, value):
        if not re.compile('^\d{11}$').match(value):
            raise ValidationError("手机号码格式错误")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'thumbnail',
                  'is_admin',
                  'is_active')


class UserPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'password',
                  'is_staff',
                  'is_admin',
                  'is_active')

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save(**validated_data)
        return instance
