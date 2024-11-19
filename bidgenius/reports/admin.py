from django.contrib import admin
from .models import SuccessAuctions

class SuccessAuctionsAdmin(admin.ModelAdmin):
    list_display = ('auction', 'bidder', 'bid_amount', 'bidder')

# Register your models here.
admin.site.register(SuccessAuctions, SuccessAuctionsAdmin)