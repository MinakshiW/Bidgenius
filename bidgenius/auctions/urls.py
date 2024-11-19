from django.urls import path
from .views import send_mail_view, add_to_successful_auction_view, add_to_all_auctions_view, add_to_closing_bid_view
from auctions.api import *



urlpatterns = [
    path('auctiondetail/',AuctionDetailsGenericView.as_view()),
    path('bidders/',BiddersView.as_view()),
    path('bidders/', BiddersByOwnerView.as_view(), name='bidders-by-owner'),
    path('manualbid/', ManualBiddingView.as_view(), name='manual-bidding'),
    path('lastbid/<int:auction_id>/', LastBidView.as_view(), name='last-bid'),
    path('auctions/automatic_mail/', send_mail_view),
    path('auctions/add_to_success/', add_to_successful_auction_view),
    path('auctions/add_to_all/', add_to_all_auctions_view),
    path('bids/closing_bids/', add_to_closing_bid_view)
    
]