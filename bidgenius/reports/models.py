from django.db import models

class SuccessAuctions(models.Model):
    auction = models.OneToOneField('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='auctions')
    bidder = models.ForeignKey('auctions.Bidders', on_delete=models.CASCADE, related_name='s_bidder')
    bid_amount = models.FloatField()
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='s_owner')

class CancelledAuctions(models.Model):
    CANCEL_CHOICES = [
        ('owner', 'owner'),
        ('admin', 'admin'),
    ]
    auction = models.OneToOneField('auctions.AuctionDetails', on_delete=models.CASCADE, related_name='c_auctions')
    cancellation_reason = models.TextField()
    cancelled_by = models.CharField(max_length=10,choices=CANCEL_CHOICES)
