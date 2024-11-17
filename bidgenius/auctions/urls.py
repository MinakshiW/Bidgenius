from django.urls import path
from .views import send_mail_view, add_to_successful_auction_view, add_to_all_auctions_view, add_to_closing_bid_view

urlpatterns = [
    path('auctions/automatic_mail/', send_mail_view),
    path('auctions/add_to_success/', add_to_successful_auction_view),
    path('auctions/add_to_all/', add_to_all_auctions_view),
    path('bids/closing_bids/', add_to_closing_bid_view)
]