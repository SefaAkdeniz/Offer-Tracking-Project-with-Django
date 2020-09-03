from django.contrib import admin
from .models import Offer

# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    list_display = ('customer', 'personel', 'machine', 'status','offer_file','offer_date')
    list_display_links = ('customer', 'personel', 'machine','offer_file','offer_date')
    list_filter = ('customer', 'personel', 'machine', 'status','offer_file','offer_date')
    list_editable = ('status',)
    search_fields = ('customer', 'personel', 'machine', 'status','offer_file','offer_date')
    list_per_page = 10

admin.site.register(Offer,OfferAdmin)