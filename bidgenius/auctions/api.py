from rest_framework import generics,status
from rest_framework.response import Response
from auctions.models import AuctionDetails,Bidders,CurrentBids
from auctions.serializers import AuctionDetailSerializer,BiddersSerializer,CurrentBidsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AuctionDetailsGenericView(generics.ListCreateAPIView):
    serializer_class = AuctionDetailSerializer
    queryset = AuctionDetails.objects.all()

class BiddersView(generics.ListCreateAPIView):
    serializer_class = BiddersSerializer
    queryset = Bidders.objects.all()


class BiddersByOwnerView(generics.ListAPIView):
    serializer_class = BiddersSerializer

    def get_queryset(self):
        owner_id = self.request.query_params.get('owner')  
        if owner_id is not None:
            return Bidders.objects.filter(bidder_id=owner_id)  
        return Bidders.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            return super().list(request, *args, **kwargs)
        return Response([], status=200) 

class ManualBiddingView(generics.CreateAPIView):
    """
    View for placing manual bids
    """
    queryset = CurrentBids.objects.all()
    serializer_class = CurrentBidsSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        bid_amount = request.data.get('bid_amount')
        auction_id = request.data.get('auction')
        bidder_id = request.data.get('bidder')

        # Fetch the auction and the last/current bid
        try:
            auction = AuctionDetails.objects.get(auction_id=auction_id)
        except AuctionDetails.DoesNotExist:
            return Response({"error": "Auction not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get the latest bid amount
        last_bid = CurrentBids.objects.filter(auction=auction).order_by('-bid_amount').first()
        if last_bid and bid_amount <= last_bid.bid_amount:
            return Response({"error": "Bid must be greater than the last bid"}, status=status.HTTP_400_BAD_REQUEST)

        # Process the new bid
        bidder = Bidders.objects.get(pk=bidder_id)
        bid = CurrentBids.objects.create(bid_amount=bid_amount, bidder=bidder, auction=auction)

        return Response({"message": "Bid placed successfully", "latest_bid": bid_amount}, status=status.HTTP_201_CREATED)

class LastBidView(generics.RetrieveAPIView):
    """
    View to get the latest bid for a specific auction
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, auction_id):
        try:
            auction = AuctionDetails.objects.get(auction_id=auction_id)
        except AuctionDetails.DoesNotExist:
            return Response({"error": "Auction not found"}, status=status.HTTP_404_NOT_FOUND)

        last_bid = CurrentBids.objects.filter(auction=auction).order_by('-bid_amount').first()

        if last_bid:
            return Response({"latest_bid": last_bid.bid_amount}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No bids yet"}, status=status.HTTP_200_OK)
