from rest_framework import serializers
from .models import BooksModel


class BooksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    pages = serializers.IntegerField()
    in_stock = serializers.IntegerField()
    subtitle = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=13)

    def validate(self, attrs):
        isbn = attrs.get('isbn')
        if BooksModel.objects.filter(isbn=isbn).exists():
            raise serializers.ValidationError("This ISBN is already in use.")
        elif len(isbn) != 13:
            raise serializers.ValidationError("ISBN should have 13 digits.")
        elif not isbn.isnumeric():
            raise serializers.ValidationError("ISBN should have only digits.")

        pages = attrs.get('pages')
        if pages <= 0:
            raise serializers.ValidationError("Pages should be greater than 0.")
        return attrs

    def create(self, validated_data):
        return BooksModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.content = validated_data.get('content', instance.content)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance
