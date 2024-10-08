from django.db import models

class AuctionDetails(models.Model):
    product = models.OneToOneField('seller.ProductInformation', on_delete=models.CASCADE, related_name='auction')
    auction_id = models.BigAutoField(primary_key=True)
    auction_date = models.DateField(blank=True)
    auction_start_time = models.TimeField(blank=True)
    auction_end_time = models.TimeField(blank=True)
    increment_amount = models.FloatField(blank=True)

    def __str__(self) -> str:
        return f'{self.auction_id}'
    
class CurrentAuctions(models.Model):
    current_auction_id = models.BigAutoField(primary_key=True)
    auction = models.OneToOneField('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='current_auction')

class Bidders(models.Model):
    CHOICES = [('automatic', 'automatic'), ('manual', 'manual')]
    bidder_type = models.CharField(max_length=10, choices=CHOICES)
    bidder = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='bidders')

class AutomaticBidding(models.Model):
    max_bid_amount = models.FloatField(blank=True)
    inc_amount = models.FloatField(blank=True)
    bidder = models.ForeignKey('auctions.Bidders', on_delete=models.CASCADE, related_name='autobids')
    auction = models.ForeignKey('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='auction_autobids')

class CurrentBids(models.Model):
    bid_amount = models.FloatField()
    bidder = models.ForeignKey('auctions.Bidders', on_delete=models.CASCADE, related_name='currentbids')
    auction = models.ForeignKey('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='auctionbids')

class AllBids(models.Model):
    bid_amount = models.FloatField()
    bidder = models.ForeignKey('auctions.Bidders', on_delete=models.CASCADE, related_name='allbids')
    auction = models.ForeignKey('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='allauctionbids')

class ClosingBid(models.Model):
    closing_bid_amount = models.FloatField()
    bidder = models.ForeignKey('auctions.Bidders', on_delete=models.CASCADE, related_name='closing_Bids')
    auction = models.ForeignKey('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='closing_auctions')