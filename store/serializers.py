from rest_framework import serializers
from .models import Product, Category, ProductImages


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'parent']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    images = ProductImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price',
                  'category', 'discount', 'discount_price', 'images']
