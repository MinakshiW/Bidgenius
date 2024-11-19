from django.urls import path
from auctions.api import *



urlpatterns = [
    path('auctiondetail/',AuctionDetailsGenericView.as_view()),
    path('bidders/',BiddersView.as_view()),
    path('bidders/', BiddersByOwnerView.as_view(), name='bidders-by-owner'),
    path('manualbid/', ManualBiddingView.as_view(), name='manual-bidding'),
    path('lastbid/<int:auction_id>/', LastBidView.as_view(), name='last-bid'),
    
]