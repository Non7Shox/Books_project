from rest_framework import serializers
from .models import UsersModel


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
    age = serializers.CharField()

    def validate_age(self, age: str):
        if not age.isnumeric():
            raise serializers.ValidationError("Age must be number")
        return age

    def create(self, validated_data):
        return UsersModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
