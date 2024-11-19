from rest_framework import serializers
from auctions.models import AuctionDetails,Bidders,CurrentBids
from seller.serializers import ProductSerializer


class AuctionDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = AuctionDetails
        fields = "__all__"

class BiddersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bidders
        fields = "__all__"

class BiddersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidders
        fields = ['id', 'bidder_type', 'bidder']


class CurrentBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentBids
        fields = '__all__'