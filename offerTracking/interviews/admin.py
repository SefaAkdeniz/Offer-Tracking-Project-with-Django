from django.contrib import admin
from .models import Interviews

# Register your models here.

class InterviewsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'personel', 'interviews_type','offer_date','note')
    list_display_links = ('customer', 'personel', 'interviews_type','offer_date')
    list_filter = ('customer', 'personel', 'interviews_type','offer_date')
    list_editable = ('note',)
    search_fields = ('customer', 'personel', 'interviews_type','offer_date','note')
    list_per_page = 10

admin.site.register(Interviews,InterviewsAdmin)