from django.contrib import admin
from .models import AuctionDetails, CurrentAuctions, Bidders, CurrentBids, AllBids, ClosingBid

class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display = ('auction_id', 'auction_date')

class CurrentAuctionsAdmin(admin.ModelAdmin):
    list_display = ('current_auction_id', 'auction')
    
class BiddersAdmin(admin.ModelAdmin):
    list_display = ('bidder',)
    
class CurrentBidsAdmin(admin.ModelAdmin):
    list_display = ('bid_amount', 'bidder', 'auction')

class AllBidsAdmin(admin.ModelAdmin):
    list_display = ('bid_amount', 'bidder', 'auction')
    
class ClosingBidsAdmin(admin.ModelAdmin):
    list_display = ('closing_bid_amount', 'bidder', 'auction')  

# Register your models here
admin.site.register(AuctionDetails, AuctionDetailsAdmin)
admin.site.register(CurrentAuctions, CurrentAuctionsAdmin)
admin.site.register(Bidders, BiddersAdmin)
admin.site.register(CurrentBids, CurrentBidsAdmin)
admin.site.register(AllBids, AllBidsAdmin)
admin.site.register(ClosingBid, ClosingBidsAdmin)