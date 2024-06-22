from rest_framework import serializers
from .models import AuthorsModels


class AuthorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=13)
    email = serializers.EmailField()
    age = serializers.IntegerField()

    def validate_phone_number(self, phone_number):
        if AuthorsModels.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError()
        elif len(phone_number) != 13:
            raise serializers.ValidationError("ISBN should have 13 digits.")
        return phone_number

    def create(self, validated_data):
        return AuthorsModels.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
