from django.db import models
from customer.models import Customer
from machine.models import Machine

# Create your models here.

STATUS_CHOICES = (
    (1, 'BEKLEMEDE'),
    (2, 'İPTAL'),
    (3, 'SATILDI'),
    (4, 'KAYIP'),  
)

class Offer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Firma')
    personel = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name='Sorumlu Personel')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Tezgah')
    offer_number =models.CharField(max_length=20, verbose_name="Teklif Kodu",unique=True)
    status = models.PositiveSmallIntegerField( choices=STATUS_CHOICES, verbose_name="Durum",default=1)
    offer_file = models.FileField(upload_to='uploads/%Y/%m/%d/',verbose_name='Rapor')
    offer_date = models.DateTimeField(auto_now_add=True, verbose_name="Teklif Tarihi")
    note = models.TextField(verbose_name="Teklif Notu",blank=True)

    def __str__(self):
        return self.customer.company_name+"-"+self.offer_number

    class Meta:
        verbose_name = 'Teklif'
        verbose_name_plural = 'Teklifler'

