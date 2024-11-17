from rest_framework import serializers
from .models import *
from accounts.serializers import UserSerializer
from datetime import datetime

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

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

class ProductImagesSerializer(serializers.ModelSerializer):
    Product = ProductInformationSerializer(read_only = True)
    class Meta:
        model = ProductImages
        fields = '__all__'   