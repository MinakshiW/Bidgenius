from django.shortcuts import render
from .tasks import send_mail_function, add_to_successful_auctions, add_to_all_auctions, add_to_closing_bids
from django.http import HttpResponse

def send_mail_view(request):
    send_mail_function()
    return HttpResponse('Mail sent successfully......')

def add_to_successful_auction_view(request):
    add_to_successful_auctions()
    return HttpResponse('Added to successfull auction')

def add_to_all_auctions_view(request):
    add_to_all_auctions()
    return HttpResponse('Added to all auctions successfully....')

def add_to_closing_bid_view(request):
    add_to_closing_bids()
    return HttpResponse('Added to Closing  Bids Successfully...')