from rest_framework import serializers
from ..models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields
class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields

class BookRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields

class BookCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields

def validate(self, attrs):
    return super().validate(attrs)

def create(self, validated_data):
    return super().create(validated_data)

def update(self, instance, validated_data):
    return super().update(instance, validated_data)

# Converts json to python validated data
def to_internal_value(self, data):
    return super().to_internal_value(data)

# Converts python validated data to json / opposite of to_internal_value
def to_representation(self, instance):
    return super().to_representation(instance)

