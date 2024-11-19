from celery import shared_task
from django.conf import settings
from auctions.utils import async_send_email
from datetime import date
from django.db.models import Max
from django.db import connection

from .models import AuctionDetails, CurrentAuctions, CurrentBids, Bidders, AllBids, ClosingBid
from reports.models import SuccessAuctions


@shared_task(bind = True)
def send_mail_function(self):
    print('main fun called_____')
    
    today = date.today()
    auctions_today = AuctionDetails.objects.all().filter(auction_date=today)
    print(auctions_today)

    for auction in auctions_today:
        print(auction)
        print(auction.auction_id, auction.product.owner.email)
        print('loop started.....')
        async_send_email(
            subject='Auction Reminder',
            message=f'You have auction today. Please make sure to attend. Here is the link http://127.0.0.1:3000/user/auctions/{auction.auction_id}/',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list= [auction.product.owner.email],

        )
    return 'mail sent successfully...'



@shared_task(bind = True)
def add_to_successful_auctions(self):
    print('main fun called_____')
    
    current_auctions = CurrentAuctions.objects.all()
    print(current_auctions)

    for auction_obj in current_auctions:
        # max_bid = CurrentBids.objects.filter(auction=auction_obj.auction).aggregate(max_bid=Max('bid_amount'))['max_bid']

        max_bid = auction_obj.auction.auctionbids.all().aggregate(max_bid=Max('bid_amount'))['max_bid']
        print(max_bid)

        max_bid_obj = CurrentBids.objects.get(auction=auction_obj.auction, bid_amount = max_bid)

        # max_bid_obj = auction_obj.auction.auctionbids.get(bid_amount = max_bid)

        Success_auction = SuccessAuctions(auction = max_bid_obj.auction,
                                          bidder = max_bid_obj.bidder,
                                          bid_amount = max_bid_obj.bid_amount,
                                          owner = auction_obj.auction.product.owner)
        
        Success_auction.save()

        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE {CurrentAuctions._meta.db_table}")
            cursor.execute(f"TRUNCATE TABLE {CurrentBids._meta.db_table}")


    return 'auctions added successfully...'



@shared_task(bind = True)
def add_to_all_auctions(self):
    print('main fun called_____')
    
    current_auctions = CurrentAuctions.objects.all()
    print(current_auctions)

    for auction_obj in current_auctions:
        # max_bid = CurrentBids.objects.filter(auction=auction_obj.auction).aggregate(max_bid=Max('bid_amount'))['max_bid']

        current_bids_obj = auction_obj.auction.auctionbids.all()

        for current_bid in current_bids_obj:
            all_bids = AllBids(
                                auction = current_bid.auction,
                                bidder = current_bid.bidder,
                                bid_amount = current_bid.bid_amount
                            )   
        
            all_bids.save()

    return 'auctions added to all bidstable successfully...'


@shared_task(bind = True)
def add_to_closing_bids(self):
    print('main fun called_____')
    
    current_auctions = CurrentAuctions.objects.all()
    print(current_auctions)

    for auction_obj in current_auctions:
        max_bid = CurrentBids.objects.filter(auction=auction_obj.auction).aggregate(max_bid=Max('bid_amount'))['max_bid']
        print(max_bid)

        highest_bids_obj = auction_obj.auction.auctionbids.get(bid_amount=max_bid)
        print(highest_bids_obj)
        high_bids = ClosingBid(
                                auction = highest_bids_obj.auction,
                                bidder = highest_bids_obj.bidder,
                                closing_bid_amount = highest_bids_obj.bid_amount
                            )   
        
        high_bids.save()
    return 'closing bid added successfully...'

