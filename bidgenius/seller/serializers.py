from rest_framework import serializers
"""from seller.models import ProductCategory,ProductInformation,ProductImages"""
from accounts.serializers import UserSerializer

from .models import *
from datetime import datetime


class ProductImagesReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('product_image',)

class ProductSerializer(serializers.ModelSerializer):
    product_imagess = ProductImagesReadOnlySerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = ProductInformation
        fields = '__all__'

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInformation
        fields = "__all__"


class ProductImagesSerializer(serializers.ModelSerializer):
    product = ProductInfoSerializer(read_only = True)
    class Meta:
        model = ProductImages
        fields = '_all_'

class ProductImageSerializer(serializers.ModelSerializer):
    # product_image = serializers.ListField(child=serializers.FileField(),write_only=True)
    product = ProductInfoSerializer(read_only=True)
    owner = serializers.CharField(source='product.owner', read_only=True)
    class Meta:
        model = ProductImages
        fields = ('product_image','product','owner')
        
    def create(self, validated_data):
        product_image = validated_data.pop('product_image')
        product = ProductInformation.objects.create(**validated_data)
        for pro_img in product_image:
            obj = ProductImages.objects.create(product=product, product_image=pro_img)
        return product

    # def create(self, validated_data):
    #     product_image = validated_data.pop('product_image')
    #     product = ProductInformation.objects.create(**validated_data)
    #     for pro_img in product_image:
    #         print(pro_img)
    #         obj = ProductImages.objects.create(product=product,product_image=pro_img)
    #     return product

  
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductInformationSerializer(serializers.ModelSerializer):
    product_added_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M', read_only=True)
    ProductCategory = ProductCategorySerializer(read_only= True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = ProductInformation
        
        fields = '__all__'

    # def create(self, validated_data):
    #     # Set the current time for product_added_time
    #     validated_data['product_added_time'] = datetime.now()
    #     print(validated_data)
    #     return super().create(validated_data)

class ProductImagessSerializer(serializers.ModelSerializer):
    Product = ProductInformationSerializer(read_only = True)
    class Meta:
        model = ProductImages
        fields = '__all__'   

