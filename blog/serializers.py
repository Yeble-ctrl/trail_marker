from blog import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        exclude = ['owner']

    def create(self, validated_data):
        return models.Blog.objects.create(**validated_data)

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogPost
        exclude = ['blog']

    def create(self, validated_data):
        return models.BlogPost.objects.create(**validated_data)

class BlogPostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogPostPhoto
        exclude = ['owner']

    def create(self, validated_data):
        return models.BlogPostPhoto.objects.create(**validated_data)