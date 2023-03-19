from rest_framework import serializers
from .models import Image
from django.contrib.auth.models import User

class ImageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'description', 'created_on', 'updated_on'] 

class ImageDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image