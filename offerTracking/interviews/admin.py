from django.contrib import admin
from .models import Interviews

# Register your models here.

class InterviewsAdmin(admin.ModelAdmin):
    list_display = ('offer', 'personel', 'interviews_type','offer_date','note')
    list_display_links = ('offer', 'personel', 'interviews_type','offer_date')
    list_filter = ('offer', 'personel', 'interviews_type','offer_date')
    list_editable = ('note',)
    search_fields = ('offer__customer__company_name', 'personel__username', 'interviews_type','offer_date','note')
    list_per_page = 10

admin.site.register(Interviews,InterviewsAdmin)