from rest_framework import serializers
from .models import AuctionDetails
from seller.serializers import ProductInformationSerializer

class AuctionDetailsSerializer(serializers.ModelSerializer):
    product = ProductInformationSerializer(read_only=True)
    class Meta:
        model = AuctionDetails
        fields = '__all__'